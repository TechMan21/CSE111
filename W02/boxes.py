import math

print("Hello. I am your program assistant Jake. I am here to help you know how many boxes you will need for todays shipments.")
print()
user_input1= int(input("Please enter the amount of items that will be boxed up and shipped today: "))
user_input2 = int(input("Please enter the number of items that can fit per box: "))
print("Note: Sorry that I am not advanced anough to calculate more specific to the orders.")
print()

boxes = user_input1 / user_input2
print(f"You will need approximately {math.ceil(boxes)} boxes for todays shipments.")


'''A manufacturing company needs a program that will help its employees
 pack manufactured items into boxes for shipping. Write a Python program
  named boxes.py that asks the user for two integers: 1) the number of manufactured
   items and 2) the number of items that the user will pack per box. Your program must 
   compute and print the number of boxes necessary to hold the items. This must be a whole 
   number. Note that the last box may be packed with fewer items than the other boxes.'''