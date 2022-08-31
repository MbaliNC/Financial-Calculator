# Capstone Project 1
# create a program that allows the user to access two different financial calculators:
# an investment calculator and a home loan repayment calculator
# declare and initialize the variables
# 'r' is the interest rate entered and divided by 100 to turn into decimal format
# 'P' is the prinipal amount that the user deposits/invests
# 't' is the number of years that the money is being invested for
import math 
# this first part of the program will be required to use simple and compound interest formulas
# simple interest: total = amount (1 + interest rate * number of years)
# compound interest: total = amount (1 + interest rate ** number of years)

# Choose either 'investment' or 'bond' from the menu below to proceed
# used 3 quotation marks for multi-line string
print("Hello, Welcome to your Financial Calculator.")
print('''Choose either 'Investment' or 'Bond' as a financial calculator from the menu below to proceed:
-------- Investment ------- to calculate the amount of interest you will earn in interest
-------- Bond ------------- to calcualte the amount you will have to pay on a home loan''') 

# the first calculation is for an investment calculator
# ask the user for the values needed to calculate the interest rate payments in years
investment_or_bond = str(input("Do you choose investment or bond? ")).lower()

# user will either choose investment or bond financial calculator
# user will either choose simple or compound interest
if investment_or_bond == "investment":

    P = float(input("How much money would you like to be invested? "))
    r = float(input("Enter the interest rate in %: ")) 
    r = r/100   # calculating the interest rate to a decimal number
    t = float(input("How many years would you like to invest? "))

    simple_or_compound_interest = str(input("Do you choose simple or compound interest? ")).lower()

    if simple_or_compound_interest == "simple":
      
        simple_interest = round(P*(1+r*t), 2)        # using the round() to round up to 2 decimal places
        print(f"Your interest rate over {t} years will be R{simple_interest}")
    elif simple_or_compound_interest == "compound":
        compound_interest = round(P*math.pow((1+r),t), 2)
        print(f"Your interest rate over {t} years will be R{compound_interest}")
    else:
        print("Please choose an appopriate option")
    
        

# user will either choose investment or bond, in this case, lets choose bond
# this program will calculate how much the user will pay monthly from choosing a bond
# 'P' is the present value of the house
# 'i' is the monthly interest rate by dividing the annual interest rate by 12
# 'n' is the number of months which the bond will be repaid
# declare and intialize the variables
# bond repayment formuale
# repayment = (monthly interest rate x present value of house) / (1-(1+ monthly interest rate)) - number of months
# the second calculation is for a home loan repayment calculator
elif investment_or_bond == "bond":
    P = float(input("What is the current value of your house? "))
    i = float(input("What is the interest rate? "))
    n = float(input("How many months do you plan to pay? "))

    i = i/100    # calculating the monthly interest to convert to decimal
    i = i/12
    bond_repayment = round((i*P)/(1-(1+i)**(-n)), 2)   
    
    print(bond_repayment)
    print(f"Your monthly repayment over {n} years will be R{bond_repayment}")
else:
    print("Please enter appropriate information")
print("Thank you for using our Financial Calculator.")

