#!/usr/bin/env python
import pika
import json
import ledger-cli

if __name__ == '__main__':
    import click

    @click.command()
    @click.option("-q", "--queue_name", default="", help="Name of the node's queue.  Must be unique across all nodes.")
    def run(queue_name): 

        # Basic sanity checks on inputs
        if not queue_name or queue_name is "":
            print("Invalid queue_name param")
            return

        # Set up the rabbitmq connection and ensure the exchange is there
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.exchange_declare(exchange='transactions', type='fanout')

        # Used specified queue name and make it durable so messages will be there if disconnect happens
        result = channel.queue_declare(queue=queue_name, durable=True)
        queue_name = result.method.queue

        channel.queue_bind(exchange='transactions',
                        queue=queue_name)

        print(' [*] Waiting for logs. To exit press CTRL+C')

        def callback(ch, method, properties, body):
            
            # Parse the message into a dict
            message = json.loads(body)

            # Post it to SQL using the cli tool
            ledger-cli.post_transaction_to_db(message['transaction_date'], message['description'], message['from_acct'], message['to_acct'], message['amount'])

        channel.basic_consume(callback,
                            queue=queue_name,
                            no_ack=True)

        channel.start_consuming()

    run()        