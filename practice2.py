"""
Title:		practice2.py
Purpose:	livehack3 practice question

Author: Lydia He

Created: January 6 2021
"""
total = 0
days = 0
done = True

while done:
  daily_amount = float(input("Enter a daily spent amount (-1 to stop): "))

  if daily_amount == -1:
    done = False
  else:
    total = total + daily_amount
    days = days + 1
print("Total Days travelled: " + str(days))
print("Total amount spent: $" + str(total))

if (total * days) > (days * 250):
  fee = total * 0.13
  print("You owe a fee of: $" + str(fee))
else:
  print("Phew, you do not owe a fee")