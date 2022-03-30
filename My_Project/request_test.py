import random
import json
import pip._vendor.requests 

def random_movie():
    '''Use the the random module to use a random movie_id in the 
        curl command with Marcelo's code to get one of the movies in the list'''
    #It for some reason is not liking randint...even though it is imported
    
    headers = {
        'accept': 'application/json',
    }
    random_integer = random.randint(0, 27)
    response1 = pip._vendor.requests.get(f'https://mcuapi.herokuapp.com/api/v1/movies/{random_integer}', headers=headers)
    json_data = json.loads(response1.text)
    print(json_data["title"])
    # for dictionary in json_data:
    #     print(dictionary)

random_movie()