import calendar
from datetime import date
from datetime import datetime
#^imports the date/day of the week

subtotal = float(input("Enter the subtotal of the transaction: "))
# sales_tax = 0.06
# discount = 0.10

current_date = datetime.now()
day_of_week = date.weekday(current_date)
#^in weekday function, the day shows in numbers. 0 = Monday and Sunday is 6. 1 = Tuesday, 2= Wednesday.
if day_of_week == (1) or (2) and subtotal >= 50:
    discount = subtotal * 0.10
    subtotal -= discount
    print(f"Your discount: {discount:.2f}")
    # pre_total = subtotal - (subtotal * discount)
    # total = pre_total + (pre_total * 0.06)
    
# else:#     print("error")
tax = subtotal * 0.06
total = subtotal + tax

print(f"Sales Tax: {tax:.2f}")
print(f"Your total is: {total:.2f}")