import csv
from datetime import datetime
from tabulate import tabulate


class Transaction:
    """An object representing a transaction for the specified party
    with a credit/debit amount on a specified date"""
    def __init__(self, date, credit, debit, party):
        self.date = date
        self.credit = credit
        self.debit = debit
        self.party = party

    def __str__(self):
        return "%s %s %s %s" % (self.date, self.credit, self.debit, self.party)

    __repr__ = __str__


class Account:
    """"An object representing the account of a person. In contains all the transactions for that person"""
    def __init__(self, name):
        self.person_name = name
        self.transactions = []

    def add_transactions(self, changes):
        if type(changes) is list:
            self.transactions.extend(changes)
        else:
            self.transactions.append(changes)
        self.transactions.sort(key=lambda o: o.date)

    def balance_to_date(self, date):
        balance = 0
        i = 0
        while i < len(self.transactions):
            entry = self.transactions[i]
            if entry.date > date:
                break

            balance += entry.debit
            balance -= entry.credit
            i += 1
        return balance

    def print(self):
        tab_data = []
        for entry in self.transactions:
            tab_data.append([entry.date.strftime('%Y-%m-%d'), '§' + str(entry.debit), '§' + str(entry.credit), entry.party])
        print(tabulate(tab_data, headers=['Date', 'In', 'Out', 'Party'], tablefmt='grid'))


class Ledger:
    """An object representing a ledger: it contains accounts for parties.
    It can read files to add further transactions"""
    def __init__(self):
        self.balance_sheets = {}

    def is_valid_row(self, row):
        return len(row) == 4 and len(row[1]) > 0 and len(row[2]) > 0 and row[3].replace('.','',1).isdigit()

    def readfile(self, filename):
        transactions = []
        with open(filename) as csvfile:
            # date,from,to,amount
            reader = csv.reader(csvfile, delimiter = ',')
            for row in reader:
                if self.is_valid_row(row):
                    date = datetime.strptime(row[0], '%Y-%m-%d')
                    debtor = row[1]
                    creditor = row[2]
                    amount = float(row[3])
                    if not debtor in self.balance_sheets:
                        self.balance_sheets[debtor] = Account(debtor)
                    self.balance_sheets[debtor].add_transactions(Transaction(date, amount, 0, creditor))
                    if not creditor in self.balance_sheets:
                        self.balance_sheets[creditor] = Account(creditor)
                    self.balance_sheets[creditor].add_transactions(Transaction(date, 0, amount, debtor))

    def balance_to_date(self, party, date):
        return self.balance_sheets[party].balance_to_date(date)

    def print_for_party(self, party):
        if party not in self.balance_sheets:
            raise ValueError(party + ' not found in the ledger')
        account = self.balance_sheets[party]
        print("Account for " + party)
        account.print()

    def print(self):
        for party, account in self.balance_sheets.items():
            print("Account for " + party)
            account.print()

if __name__ == "__main__":
    l = Ledger()
    l.readfile('resources/input0.txt')
    l.print()
    print("John's balance on 17th January 2015: ")
    print(l.balance_to_date('john', datetime.strptime('2015-01-17', '%Y-%m-%d')))
