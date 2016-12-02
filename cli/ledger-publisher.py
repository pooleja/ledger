#!/usr/bin/env python
import pika
import sys
import datetime
import json

if __name__ == '__main__':
    import click

    @click.command()
    @click.option("-d", "--description", default="", help="Description for the transaction. Ex: \"Trader Joes\"")
    @click.option("-f", "--from_acct", default="", help="Account to be debited. Ex: Assets:Checking")
    @click.option("-t", "--to_acct", default="", help="Account to be credited. Ex: Expenses:Groceries")
    @click.option("-a", "--amount", default=0, help="Amount of the transaction in dollars. Ex: 100")
    def run(description, from_acct, to_acct, amount):     

        # Basic sanity checks on inputs
        if not from_acct or from_acct is "":
            print("Invalid from_acct param")
            return

        if not to_acct or to_acct is "":
            print("Invalid to_acct param")
            return

        if amount is 0:
            print("Invalid amount param")
            return   

        # Build the message dictionary from params
        message = {}
        message['transaction_date'] = str(datetime.datetime.now())
        message['description'] = description
        message['from_acct'] = from_acct
        message['to_acct'] = to_acct
        message['amount'] = amount

        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.exchange_declare(exchange='transactions', type='fanout')
        
        channel.basic_publish(exchange='transactions',
                        routing_key='',
                        body=json.dumps(message))

        print(" [x] Sent %r" % message)
        connection.close()
    
    run()
