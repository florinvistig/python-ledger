#Ledger app

Defines a Ledger object that accepts input as text files and can print the accounts of all involved parties in the imported transactions.

In resources/ folder, there are a number of sample input text files.
You can check the test_app.py how they are used.

To create a new Ledger:

`l = Ledger()`

To read a file of transactions:

`l.readfile('input.txt')`

Example of input file:
```
2015-01-16,john,mary,125.00
2015-01-17,john,supermarket,20.00
2015-01-17,mary,insurance,100.00
```

You can then print the whole ledger:

`l.print()`

Or, you can print for a specific party:

`l.print_for_party('john')`

Which will print the Account for John in the following format:
```
Account for john
+------------+------+--------+-------------+
| Date       | In   | Out    | Party       |
+============+======+========+=============+
| 2015-01-16 | §0   | §125.0 | mary        |
+------------+------+--------+-------------+
| 2015-01-17 | §0   | §20.0  | supermarket |
+------------+------+--------+-------------+
```

To find out the balance for an account at a specific date:

`print(l.balance_to_date('john', datetime.strptime('2015-01-17', '%Y-%m-%d')))`

Which will print:

```
John's balance on 17th January 2015: 
-145.0
```

### To generate further input files

You can use the generate_transactions.py file to generate a random input file. The code in this script isn't the most beautiful, but it works...
