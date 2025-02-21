# Exercise 1:
# Write a program to calculate salary. Take input for employee name, rate and weekly hours.
# Then calculate tax using:
# if rate > 45 then the tax is 0.02
# if rate <= 45 then the tax is 0.01
# Output the results with the employee’s salary and the amount of tax they will pay.

employee_name = input("enter employee name: ")
employee_hours = input("enter hours worked: ")
employee_rate = input("enter hourly rate: ")

payrate = float(employee_rate)
hours = float(employee_hours)

if float(employee_rate) > 45:
    taxrate = 0.02
elif float(employee_rate) <= 45:
    taxrate = 0.01
else:
    print("taxrate is unknown")

grosspay = payrate * hours
withtax = grosspay*taxrate

netpay = grosspay - withtax

print("grosspay:", grosspay)
print("withholding tax:", withtax)
print("netpay:", netpay)