import csv
import datetime
import random

from faker import Faker


fake = Faker()
parties = []
numdays = 20
transactions = []
MAX_NUM_TRANSACTIONS = 10
MIN_AMOUNT = 0
MAX_AMOUNT = 1000

for i in range(0, 10):
    parties.append(fake.name())

base = datetime.datetime.today()
date_list = [base - datetime.timedelta(days=x) for x in range(0, numdays)]

for date in date_list:
    for i in range(0, random.randint(0, MAX_NUM_TRANSACTIONS)):
        debtor = parties[random.randint(0, len(parties) - 1)]
        creditor = parties[random.randint(0, len(parties) - 1)]
        while creditor == debtor:
            creditor = parties[random.randint(0, len(parties) - 1)]
        amount = random.randint(MIN_AMOUNT, MAX_AMOUNT)
        row = "{0},{1},{2},{3}".format(date.strftime('%Y-%m-%d'), creditor, debtor, amount)
        transactions.append(row)

with open('generated_input.txt', 'w') as myfile:
    wr = csv.writer(myfile)
    for row in transactions:
        print(row, file=myfile)
