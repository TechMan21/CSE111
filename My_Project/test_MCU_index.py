from random import random
import pytest
from MCU_Index import user_input_menu,random_movie,random_TV,TV_search, movie_search, print_movie_search, print_TV_search

# def test_user_input_menu():
#     assert user_input_menu() == "res = random_movie()"
#     #or "The random Marvel movie to watch is: "
#     assert user_input_menu() == "The random Marvel TV show to watch is: "

# def test_random_movie():
#     assert random_movie() == "Iron Man"
#     assert random_movie() == "Guardians of the Galaxy Vol. 2"

# def test_random_TV():
#     TV = ["Ms. Marvel", "Moon Knight", "Hawkeye", "What If...?", "Loki", "The Falcon and The Winter Soldier", "WandaVision"]
#     for _ in range(6):
#         res = random_TV()
        
#         assert res in TV

#can be much more simple for this tests
# to test for random_TV() & random_movie(), use type() to check type 
# of random_TV() & random_movie() and can use assert to check if they are strings
# or a dictionary (to prove it is getting a response from API)

def test_random_movie():
    assert random_movie() == True

def test_random_TV():
    assert random_TV() == True

def test_movie_search():
    assert type(movie_search(title_search="iron")) == dict
    assert type(movie_search(title_search="thor")) == dict
    assert type(movie_search(title_search="avenger")) == dict


def test_TV_search():
    assert type(TV_search(title_search2='loki')) == dict
    assert type(TV_search(title_search2='marvel')) == dict
    assert type(TV_search(title_search2='moon')) == dict
