#!/usr/bin/env python3
#
# Script to write transactions to postgres
#

import psycopg2

def post_transaction_to_db(transaction_date, description, from_acct, to_acct, amount):

      try:
            # Connect to the DB
            conn = psycopg2.connect("dbname='ledger' user='test5' host='localhost' password='test5'")
            print("Connected to the DB")

            # Insert the row into the DB
            cur = conn.cursor()
            cur.execute("INSERT INTO transactions (transaction_date, from_acct, from_amt, to_acct, to_amt, description) VALUES (%s, %s, %s, %s, %s, %s)", (transaction_date, from_acct, (amount * -1), to_acct, amount, description))
            conn.commit()
            cur.close()
            conn.close()
            
            print("Successfully inserted transaction record.")

      except Exception as ex:
            print("Error with DB operation {}".format(ex))


if __name__ == '__main__':
    import click

    @click.command()
    @click.option("-n", "--transaction_date", default="", help="Date when transaction was posted.")
    @click.option("-d", "--description", default="", help="Description for the transaction. Ex: \"Trader Joes\"")
    @click.option("-f", "--from_acct", default="", help="Account to be debited. Ex: Assets:Checking")
    @click.option("-t", "--to_acct", default="", help="Account to be credited. Ex: Expenses:Groceries")
    @click.option("-a", "--amount", default=0, help="Amount of the transaction in dollars. Ex: 100")
    def run(transaction_date, description, from_acct, to_acct, amount):
        """
        Runs the client.
        """

        # Basic sanity checks on inputs
        if not transaction_date or transaction_date is "":
            print("Invalid transaction_date param")
            return
            
        if not from_acct or from_acct is "":
            print("Invalid from_acct param")
            return

        if not to_acct or to_acct is "":
            print("Invalid to_acct param")
            return

        if amount is 0:
            print("Invalid amount param")
            return

        post_transaction_to_db(transaction_date, description, from_acct, to_acct, amount)
       

    run()
