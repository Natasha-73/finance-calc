# This program determines investment gain by the user if they use simple or compound interest or repayment on a bond taken out on house value

# This imports the math module
import math

# Introduces the user to what the program offers
# Wording below for investment has been changed from that in the task write up since the equation given in the tasks calculates total investment
print("""Choose either 'investment' or 'bond' from the menu below to proceed:

Investment - to calculate the total investment 
Bond       - to calculate the amount you'll have to pay on a home loan
""")

# Stores the investment type as a variable
inv_type = input("Enter your choice here: ")

# Strips any inadvertent entry of spaces in the user entry and converts to all lowercase in the instance that the user uses various cases
inv_type = inv_type.strip(" ")
inv_type = inv_type.lower()

# For option "investment", prompt the user to input further information to calculate total investment
if inv_type == "investment":
    deposit = input("Please enter your deposit amount: £")
    interest = input("Please enter the annual interest rate as a percentage: ")
    years = input("Please enter the number of years you'll like to invest you money: ")
    invest = input("Please enter if you would like your investment to gain 'simple' or 'compound' interest: ")
    
# Removes "%", "," (because some people may still put commas in their numbers)and spaces if the user inputs these
# Note that the variable 'interest' can only converted to a float after stripping "%"
    deposit = deposit.strip(" ")
    deposit = deposit.replace(",", "")
    deposit = float(deposit)
    
    interest = interest.strip("%")
    interest = interest.strip(" ")
    interest = float(interest)

    years = years.strip(" ")
    years = int(years)
        
    invest = invest.strip(" ")

# Converts to all lowercase in the instance that the user uses various cases
    invest = invest.lower()

# Converts percentage (inputted as a whole number) to a fraction
    interest = interest / 100

# Calculates and prints total investment if simple interest is chosen or else calculates total investment using compound interest and prints
    if invest == "simple":
        total = deposit * (1 + interest * years)
    else:
        total = deposit * math.pow((1+ interest), years)
    
    print(f"The value of your total investment after {years} years is £{total:.2f}")

# For option 'bond', prompt the user to input further information to calculate monthly repayment
elif inv_type == "bond":
    house_val = input("Please enter the current value of your house: £")
    interest = input("Please enter the annual interest rate as a percentage: ")
    months = input("Please enter the number of months need to repay the bond: ")

# Removes "%" "," and spaces if the user inputs these
    house_val = house_val.strip(" ")
    house_val = house_val.replace(",", "")
    house_val = float(house_val)

    interest = interest.strip("%")
    interest = interest.strip(" ")
    interest = float(interest)

    months = months.strip(" ")
    months = int(months)

# Calculates and prints monthly repayment of bond 
    interest = interest / (12 * 100)    # Convert percent annual interest rate to a monthly fraction
    repay = (interest * house_val) / (1 - math.pow((1 + interest), (-months)))

    print(f"You will have to repay £{repay:.2f} each month")

# Prints an error message if neither investment or bond were originally inputted.
else:
    print("Error: Your choice did not match either 'investment' or 'bond'.\nPlease try again.")
