import math
# the program is used to calculate the bond or investments of an individual
# first it asks them to enter what they would like to do
print("what would you like to do today. \n investment(calculate potential interest on an investment) or \n bond(calculate your home loan repayments) ")
# it converts their output to lowercases so it can recognise the input in every key entered
choice = input("choose bond or investment : ").lower()
if choice == 'bond':
    # if user enters bond it asks them to enter the value of the house they would like to buy
    house_value = float(input("please enter the current value of the house: "))
    # asks user to enter interest rate
    rate = float(input("please enter the current annual interest rate : "))
    # converts the annual interest into monthly interest
    rate = rate / float(12)
    duration = float(input("how many months do you plan on paying your bond"))
    # calculates the bond repayment
    Bond_repayment = (rate * house_value) / (1 - (1 + rate) ** (-duration))
    Bond_repayment = round(Bond_repayment, 2)
    # programs displays bond repayment
    print(f'your bond repayment is R{Bond_repayment}')
elif choice == 'investment':
    # program asks the user how much they want to invest
    initial_investment = float(input("how much would like to invest : "))
    # asks their desired interest rate
    rate = input("what rate would like to receive")
    rate = float(rate)/float(100)
    # asks the user how long they want to invest
    duration = float(input("how long would like to invest"))
# asks user if they prefer simple or compound interest
type_of_interest = input("choose your preferred interest : ").lower()
if type_of_interest == 'compound':
    # calculates how much the user would earn if they choose compound interest
    # converts every key into lowercase
    roi = (initial_investment * math.pow((float(1)+rate), (duration)))
    # rounds off answer to 2 decimal places
    roi = round(roi, 2)
    # displays potential return on investment
    print(f'your return on investment is R{roi}')
elif type_of_interest == 'simple':
    # calculates how much the user would earn if they choose simple interest
    # converts every key into lowercase
    roi = (initial_investment*(float(1+rate*duration)))
    # rounds off answer to 2 decimal places
    roi = round(roi, 2)
    # displays potential return on investment
    print(f'your return on investment is R{roi}')
