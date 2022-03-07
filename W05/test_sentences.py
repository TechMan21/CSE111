import pytest
from sentences import *
import random




def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["two", "some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Get a random number between 2 and 10 inclusive.
        quantity = random.randint(2, 11)

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(quantity)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

#     assert test_get_determiner(1) == word in single_determiners or plural_determiners
# assert test_get_determiner(0)
# assert test_get_determiner(0)
# assert test_get_determiner(1)
# assert test_get_determiner(1)

def test_get_noun():
    singular= ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    for _ in range(8):
        word = get_noun(1)
        assert word in singular

    plural= ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    for _ in range(7):
        word = get_noun(4)
        assert word in plural


def test_get_verb():
    past= ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    for _ in range(6):
        word = get_verb(0, 'past')
        assert word in past

    present_single = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(6):
        word = get_verb(1, 'present')
        assert word in present_single

    present_plural =["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    for _ in range(6):
        word = get_verb(0, 'present')
        assert word in present_plural

    future = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    for _ in range(5):
        word = get_verb(0, "future")
        assert word in future

def test_preposition():
    preposition=["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    for _ in range(10):
        prep = get_preposition()
        assert prep in preposition

def test_prepositional_phrase():
    single_determiners = ["a", "one", "the"]
    plural_determiners = ["two", "some", "many", "the"]
    singular_noun= ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    plural_noun= ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    preposition=["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    for _ in range(5):
        word = get_prepositional_phrase(1)
        words = word.split(' ')

        assert words[1] in single_determiners
    
    for _ in range(5):
        word = get_prepositional_phrase(2)
        words = word.split(' ')

        assert words[2] in plural_determiners

    for _ in range(5):
        word = get_prepositional_phrase(1)
        words = word.split(' ')

        assert words[1] in singular_noun

    for _ in range(5):
        word = get_prepositional_phrase(2)
        words = word.split(' ')

        assert words[2] in plural_noun

    for _ in range(5):
        word = get_prepositional_phrase(1)
        words = word.split(' ')

        assert words[0] in preposition



def test_full_sentence():

    assert full_sentence(1, 'past')
    assert full_sentence(1, 'present')
    assert full_sentence(1, 'future')
    assert full_sentence(6, 'past')
    assert full_sentence(-2, 'present')
    assert full_sentence(0, 'future')

    
pytest.main(["-v", "--tb=line", "-rN", __file__])