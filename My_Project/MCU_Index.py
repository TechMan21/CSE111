#This is a program made for fans of the Marvel Cinematic Universe! 
#It will begin with a menu of which the user/fan will choose between: 
# Random Movie Picker, Random TV Show Picker, Movie Details w/ Title input,
#  Search a Super Hero and their movies/related movies, and potentially more.

#Maybe I should have each menu choice a function...!!..!!

import random
from random import randint
#import requests
import pip._vendor.requests 
import json
import pprint

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
        5. Exit''')
        #5. Search a Marvel Character (their movies and the ones they're in) 
        
        while True:
            try:
                first_choice = int(input("Please select an option: ")) 
                
            except ValueError:
                print("Please select a valid option.")
            break
        return first_choice
        # try:
        #     # user_menu_choice = input("Your Menu Choice: ")
        #     first_choice = int(input("Your Menu Choice: "))

        # except ValueError:
        #     print("Please enter a number 1-4")
        #     user_input_menu()

        # return first_choice 


        # return user_menu_choice



    
#menu choice #1 function    
def random_movie():
    '''Use the the random module to use a random movie_id in the 
        curl command with Marcelo's code to get one of the movies in the list'''

    random_integer = random.randint(0, 27)

    headers = {
        'accept': 'application/json',
    }
    
    response = pip._vendor.requests.get(f'https://mcuapi.herokuapp.com/api/v1/movies/{random_integer}', headers=headers)
    json_data = json.loads(response.text)
    print()
    print("The random Marvel movie to watch is: ")
    print(json_data["title"])

    return True


#Menu choice #2 function
def random_TV():
    '''Use the the random module to use a random movie_id in the 
        curl command with Marcelo's code to get one of the movies in the list'''

    random_integer2 = random.randint(0, 5)


    headers = {
        'accept': 'application/json',
    }

    response = pip._vendor.requests.get(f'https://mcuapi.herokuapp.com/api/v1/tvshows/{random_integer2}', headers=headers)
    json_data = json.loads(response.text)
    print()
    print("The random Marvel TV show to watch is: ")
    print(json_data["title"])

    #pprint.pprint(json_data["data"][0])

    return True

    #May be good to add another print to display the bio/description of the show as well.


#Menu choice #3- Search for a movie by title
def movie_search_input():
    #Get input from user on which movie they would like to search for
    title_search = input("Please enter the title of movie you would like to search for: ")

    return title_search



def movie_search(title_search):
    '''Use the the random module to use a random movie_id in the 
        curl command with Marcelo's code to get one of the movies in the list'''

    print("The program will now display the movie and its details (if typed correctly)")
    print()

    headers = {
        'accept': 'application/json',
    }

    response = pip._vendor.requests.get(f'https://mcuapi.herokuapp.com/api/v1/movies?page=1&limit=10&columns=title%2Crelease_date%2Cphase%2Coverview%2Ctrailer_url&order=chronology%2CASC&filter=title%3D{title_search}', headers=headers)
    json_data = json.loads(response.text)
    print()

    return json_data


    #print(f"The Marvel movie you searched for is: '{title_search}' ")

def print_movie_search(json_data):
    try:    
        # print(f'''
        # Movie: {json_data["title"]}
        # Release Date: {json_data["release_date"]}''')
        #json_list = json_data["data"]
        # for key, value in json_list:
        #     print(key, ' : ', value)
        # for key in json_data[{"data"}]:
        #     print(key, ' : ', json_data[key])

        # for p_id, p_info in json_data.items():
        #     print("\nPerson ID:", p_id)
        #     for key, value in p_info:
        #         #print(key + ':', value)
        #         print(value)
        print(f'''
        ---First Result: {json_data["data"][0]["title"]}---''')
        print()
        
        print("First results details: ")
    
        pprint.pprint(json_data["data"][0])
        print()
        print(f'''
        ---Second Result: {json_data["data"][1]["title"]}---''')
        print()
        
        print("Second results details: ")
    
        pprint.pprint(json_data["data"][1])
        print()
        print(f'''
        ---Third Result: {json_data["data"][2]["title"]}---''')
        print()
        
        print("Third results details: ")
    
        pprint.pprint(json_data["data"][2])
        #print(json_data) /n
        #print("Results in proper method", '[%s]'%', '.join(map(str, json_data)))
        # search_return_list = json_data
        # search_return_list.replace("")

    except (TypeError, KeyError) as error:
        # The Error "KeyError: 'title' will pop up if the search result comes back empty-
        #  meaning the title was not found in the API. For example, the user could search "bee" 
        # but there is no title for both movie and TV that has "bee" in it. This exception will help
        # output to the user that their search did not work. 
        print("Title not found. Please try a different one.")
        print()
        print('''
        Current amount of movies in API currently holds 35 titles
        and may not have all Movies included.
        Note: API includes some movies that are to come out soon in 2023.''')
        print()
    except IndexError as error:
        print("These are all the results for this search (less than three available).")

#Menu choice #4- Search for a TV show by title
def TV_search_input():
    #Get input from user on which movie they would like to search for
    title_search2 = input("Please enter the title of TV show you would like to search for: ")

    return title_search2



def TV_search(title_search2):
    '''Use the the random module to use a random movie_id in the 
        curl command with Marcelo's code to get one of the movies in the list'''
    
    print("The program will now display the movie and its details (if typed correctly)")
    print()
    headers = {
        'accept': 'application/json',
    }

    response = pip._vendor.requests.get(f'https://mcuapi.herokuapp.com/api/v1/tvshows?page=1&limit=10&columns=title%2Crelease_date%2Cphase&order=release_date%2CDESC&filter=title%3D{title_search2}', headers=headers)
    json_data = json.loads(response.text)
    print()
    # if json_data["data"] == [] and IndexError:
    #     print("Title not found. Please try a different one.")
    #     print("Reminder: TV shows category has a very small amount currently (up to 7) and may not have all TV shows included.")
    # else:
    #     print(f"The Marvel TV show you searched for is: '{title_search}' ")
    #     print(f'''
    #     ---Result: {json_data["data"][0]["title"]}---''')
            

    return json_data

def print_TV_search(json_data):
    
    if json_data["data"] == [] and IndexError:
        print("Title not found. Please try a different one.")
        print("Reminder: TV shows category has a very small amount currently (up to 7) and may not have all TV shows included.")
    else:
        print(f'''
        ---Result: {json_data["data"][0]["title"]}---''')
        print()
        
        print("Result details: ")
        pprint.pprint(json_data["data"][0])
    #print("Results in proper method", '[%s]'%', '.join(map(str, json_data)))

    #!!!!!!!!!!!!!!! need to copy the if statement like this one for tv_search and make similar one for 
    #movie_search becuase I do not have the exception print for non-matching titles for movie search


    
def main():
    res = ""
    while True:
        first_choice = user_input_menu()
        if first_choice == 1:
            json_data = random_movie()
            # print_random(json_data)
            #print(res)
        elif first_choice == 2:
            json_data = random_TV()
            # print_random(json_data)
            #print(res)

        elif first_choice == 3:
            title_search = movie_search_input()
            json_data = movie_search(title_search)
            print_movie_search(json_data)

        elif first_choice == 4:
            title_search2 = TV_search_input()
            json_data = TV_search(title_search2)
            print_TV_search(json_data)

        elif first_choice == 5:
            print("Goodbye!")
            break

        else:
            print("Menu choice failed. Try again.")

    # print(res)

    

if __name__ == "__main__":
    main()