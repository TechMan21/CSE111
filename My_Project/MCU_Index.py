#This is a program made for fans of the Marvel Cinematic Universe! 
#It will begin with a menu of which the user/fan will choose between: 
# Random Movie Picker, Random TV Show Picker, Movie Details w/ Title input,
#  Search a Super Hero and their movies/related movies, and potentially more.

#Maybe I should have each menu choice a function...!!..!!

from random import random
from random import randint
from urllib import response
#import requests
import pip._vendor.requests 
first_choice = 0

def user_input_menu():
        print(''' 
        Welcome to The MCU Index. 
        To begin the user experience, please select one of the options below:
        (Heads-up: TV Show data is not complete)
        1. Pick a Random Marvel Movie for me
        2. Pick a Radnom Marvel TV Show for me
        3. Search for a Marvel Movie
        4. Search for a Marvel TV Show
        5. Search a Marvel Charatcer (their movies and the ones they're in) ''')

        user_menu_choice = input("Your Menu Choice: ")


        # return user_menu_choice








    
    
def random_movie():
    '''Use the the random module to use a random movie_id in the 
        curl command with Marcelo's code to get one of the movies in the list'''

    rand_int = random.randint(0, 27)
    #It for some reason is not liking randint...even though it is imported

    headers = {
        'accept': 'application/json',
    }

    response1 = pip._vendor.requests.get(f'https://mcuapi.herokuapp.com/api/v1/movies/{rand_int}', headers=headers)
    print(response1)
    #requests is not working right-light pytest. Trying pip blah blah. local variables are having errors.


    
def main():
    first_choice = user_input_menu()
    response1 = random_movie()

    if first_choice == 1:
        print(response1)
    else:
        pass

if __name__ == "__main__":
    main()