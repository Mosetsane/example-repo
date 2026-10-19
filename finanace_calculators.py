import math

print("Investment - to calculate the amount of interest you'll earn on your investment")
print("Bond - to calculate the amount you'll have to pay on a home loan")
choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

if choice == "investment":
deposit = float(input("Enter the amount you are depositing: "))
rate = float(input("Enter the interest rate (as a percentage): "))
years = int(input("Enter the number of years you plan on investing: "))
interest_type = input("Do you want simple or compound interest? ").lower()

r = rate / 100

if interest_type == "simple":
total = deposit * (1 + r * years)
print(f"Your total amount after {years} years is: R{total:.2f}")
elif interest_type == "compound":
total = deposit * math.pow((1 + r), years)
print(f"Your total amount after {years} years is: R{total:.2f}")

elif choice == "bond":
house_value = float(input("Enter the present value of the house: "))
rate = float(input("Enter the interest rate: "))
months = int(input("Enter the number of months you plan to repay the bond: "))

monthly_rate = (rate / 100) / 12
repayment = (monthly_rate * house_value) / (1 - (1 + monthly_rate) ** (-months))
print(f"Your monthly repayment is: R{repayment:.2f}")

else:
print("Invalid choice. Please enter 'investment' or 'bond'.")
