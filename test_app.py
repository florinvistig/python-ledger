import unittest

from datetime import datetime
import app


class AccountTest(unittest.TestCase):
    def test_account_balance_to_date(self):
        a1 = app.Account('john')
        e1 = app.Transaction(datetime.strptime('2015-01-15', '%Y-%m-%d'), 125, 0, 'mary')
        e2 = app.Transaction(datetime.strptime('2015-01-17', '%Y-%m-%d'), 20, 0, 'supermarket')
        a1.add_transactions([e1, e2])
        self.assertEqual(a1.balance_to_date(datetime.strptime('2015-01-16', '%Y-%m-%d')), -125)
        self.assertEqual(a1.balance_to_date(datetime.strptime('2015-01-17', '%Y-%m-%d')), -145)

    def test_account_balance_to_date_unordered_set(self):
        a1 = app.Account('john')
        e1 = app.Transaction(datetime.strptime('2015-01-15', '%Y-%m-%d'), 125, 0, 'mary')
        e2 = app.Transaction(datetime.strptime('2015-01-17', '%Y-%m-%d'), 20, 0, 'supermarket')
        # unordered by date
        a1.add_transactions([e2, e1])
        self.assertEqual(a1.transactions[0], e1)
        self.assertEqual(a1.transactions[1], e2)

    def test_ledger_for_generated_input_1(self):
        l = app.Ledger()
        l.readfile('resources/generated_input_1.txt')
        #l.print()
        self.assertEqual(l.balance_to_date('Alyssa Bailey', datetime.strptime('2017-09-16', '%Y-%m-%d')), 141)
        self.assertEqual(l.balance_to_date('Alyssa Bailey', datetime.strptime('2017-09-20', '%Y-%m-%d')), -995)

    def test_ledger_for_generated_input_2(self):
        l = app.Ledger()
        l.readfile('resources/generated_input_2.txt')
        l.print()
        # test balance = 0 before time starts
        self.assertEqual(l.balance_to_date('Dustin Rocha', datetime.strptime('2000-01-01', '%Y-%m-%d')), 0)
        # test balance
        self.assertEqual(l.balance_to_date('Dustin Rocha', datetime.strptime('2017-09-28', '%Y-%m-%d')), -1604)

    def test_ledger_read_partially_invalid_input(self):
        l = app.Ledger()
        # file contains one transaction in invalid format (missing debtor), so it should ignore that trx
        l.readfile('resources/invalid_input_2.txt')
        self.assertEqual(len(l.balance_sheets), 2)

    def test_ledger_read_invalid_input(self):
        l = app.Ledger()
        # file contains one transaction in invalid format (missing debtor), so it should ignore that trx
        l.readfile('resources/invalid_input_1.txt')
        self.assertEqual(len(l.balance_sheets), 0)

if __name__ == '__main__':
    unittest.main()