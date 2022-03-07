"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""

print("Hello There!")
user_input = int(input("To find out the range your heart rate should be when excercising, please enter your age: "))
max_rate = int(220 - user_input)
low_range = int(max_rate * 0.65)
top_range = int(max_rate * 0.85)
print(f"During your workout, to strengthen your heart, try to keep your heart rate between {low_range} and {top_range}. Good luck!")
print()
extra = input("Would you also like to know the maximum rate your heart can go? Yes/No ")

if extra == "No":
    print("Have a nice day!")
elif extra == "Yes":
     print(f"Your maximum heart rate possible is: {max_rate}")
     print("Now you know. :) Have a nice day!")
else:
    print("Invalid answer. Bye!")

    #Using or in the if statements was not working. So this will have to suffice. 