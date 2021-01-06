"""
Title:		practice1.py
Purpose:	livehack3 practice question

Author: Lydia He

Created: January 6 2021
"""
"""
this program takes in the Canadian to U.S dollar exchange rate, starting price, and ending price, and then outputs a conversion table of Canadian to U.S Dollars with increments of $10
"""
# ask the user for the dollar exchange rate
exchange = float(input("Enter the Canadian to US Dollar exchange rate: "))
# ask the user for the starting value
starting = int(input("Enter the starting value: "))
# ask the user for the end value
ending = int(input("Enter the end value: "))
print("\nCan Price  --> US Price")

for i in range(starting,ending + 1,10):
  us_amount = i * exchange
  print(str(i) + " --> " + str(us_amount))

