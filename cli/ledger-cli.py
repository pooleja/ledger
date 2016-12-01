#!/usr/bin/env python3
#
# Script to write transactions to postgres
#

import psycopg2
import datetime

if __name__ == '__main__':
    import click

    @click.command()
    @click.option("-d", "--description", default="", help="Description for the transaction. Ex: \"Trader Joes\"")
    @click.option("-f", "--from_acct", default="", help="Account to be debited. Ex: Assets:Checking")
    @click.option("-t", "--to_acct", default="", help="Account to be credited. Ex: Expenses:Groceries")
    @click.option("-a", "--amount", default=0, help="Amount of the transaction in dollars. Ex: 100")
    def run(description, from_acct, to_acct, amount):
        """
        Runs the client.
        """

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

        try:
            # Connect to the DB
            conn = psycopg2.connect("dbname='ledger' user='ledger' host='localhost' password='James'")
            print("Connected to the DB")

            # Insert the row into the DB
            cur = conn.cursor()
            cur.execute("INSERT INTO transactions (transaction_date, from_acct, from_amt, to_acct, to_amt, description) VALUES (%s, %s, %s, %s, %s, %s)", (datetime.datetime.now(), from_acct, (amount * -1), to_acct, amount, description))
            conn.commit()
            cur.close()
            conn.close()
            
            print("Successfully inserted transaction record.")

        except Exception as ex:
            print("Error with DB operation {}".format(ex))

    run()