
#Using functions for all rthis would likely be more effiecient, but I am not sure how I would do all that.
print(''' 
This program is an implementation of the Rosenberg
Self-Esteem Scale. This program will show you ten
statements that you could possibly apply to yourself.
Please rate how much you agree with each of the
statements by responding with one of these four letters:

D means you strongly disagree with the statement.
d means you disagree with the statement.
a means you agree with the statement.
A means you strongly agree with the statement.''')

p1= input('I feel that I am a person of worth, at least on an equal plane with others: ') #+
p2= input('I feel that I have a number of good qualities: ') #+
n1= input('All in all, I am inclined to feel that I am a failure: ') #-
p3= input('I am able to do things as well as most other people: ') #+
n2= input('I feel I do not have much to be proud of: ') #-
p4= input('I take a positive attitude toward myself: ') #+
p5= input('On the whole, I am satisfied with myself: ') #+
n3= input('I wish I could have more respect for myself: ') #-
n4= input('I certainly feel useless at times: ') #-
n5= input('At times I think I am no good at all: ')#-

if p1 == "D":
    p1 = 0
elif p1 == "d":
    p1 = 1
elif p1 == "a":
    p1 = 2
elif p1 == "A":
    p1 = 3
else:
    print("Error, please input valid repsonse.")
    
if p2 == "D":
    p2 = 0
elif p2 == "d":
    p2 = 1
elif p2 == "a":
    p2 = 2
elif p2 == "A":
    p2 = 3
else:
    print("Error, please input valid repsonse.")

if p3 == "D":
    p3 = 0
elif p3 == "d":
    p3 = 1
elif p3 == "a":
    p3 = 2
elif p3 == "A":
    p3 = 3
else:
    print("Error, please input valid repsonse.")

if p4 == "D":
    p4 = 0
elif p4 == "d":
    p4 = 1
elif p4 == "a":
    p4 = 2
elif p4 == "A":
    p4 = 3
else:
    print("Error, please input valid repsonse.")

if p5 == "D":
    p5 = 0
elif p5 == "d":
    p5 = 1
elif p5 == "a":
    p5 = 2
elif p5 == "A":
    p5 = 3
else:
    print("Error, please input valid repsonse.")


if n1 == 'A':
    n1 = 0
elif n1 == 'a':
    n1 = 1
elif n1 == 'd':
    n1= 2
elif n1 == 'D':
    n1 = 3
else:
    print('Error, Invalid entry found.')

if n2 == 'A':
    n2 = 0
elif n2 == 'a':
    n2 = 1
elif n2 == 'd':
    n2 = 2
elif n2 == 'D':
    n2 = 3
else:
    print('Error, Invalid entry found.')

if n3 == 'A':
    n3 = 0
elif n3 == 'a':
    n3 = 1
elif n3 == 'd':
    n3= 2
elif n3 == 'D':
    n3 = 3
else:
    print('Error, Invalid entry found.')

if n4 == 'A':
    n4 = 0
elif n4 == 'a':
    n4 = 1
elif n4 == 'd':
    n4 = 2
elif n4 == 'D':
    n4 = 3
else:
    print('Error, Invalid entry found.')

if n5 == 'A':
    n5 = 0
elif n5 == 'a':
    n5 = 1
elif n5 == 'd':
    n5 = 2
elif n5 == 'D':
    n5 = 3
else:
    print('Error, Invalid entry found.')

result = p1 + p2 + p3 + p4 + p5 + n1 + n2 +n3 + n4 + n5
print(f'Here is your self-esteem score: {result}')

if result > 15:
    print('Your mental health seems pretty healthy. Good job!')
elif result <= 15:
    print('It may be good to see a doctor/therapist about your repsonses to these questions. Thank you for trying this program.')
else:
    print('Error')
