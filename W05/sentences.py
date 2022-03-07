#W05 Milestone assignment
import random
from statistics import quantiles

def main():
    word = get_determiner(1)
    noun = get_noun(1)
    verb = get_verb(1, 'past')
    p_sentence = part_sentence(1, 'past')
    print(p_sentence)
    p_sentence = part_sentence(2, 'past')
    print(p_sentence)
    p_sentence = part_sentence(1, 'present')
    print(p_sentence)
    p_sentence = part_sentence(2, 'present')
    print(p_sentence)
    p_sentence = part_sentence(1, 'future')
    print(p_sentence)
    p_sentence = part_sentence(2, 'future')
    print(p_sentence)
    prep = get_preposition()
    print()
    print()
    sentence = full_sentence(1, 'past')
    print(sentence)
    sentence = full_sentence(2, 'past')
    print(sentence)
    sentence = full_sentence(1, 'present')
    print(sentence)
    sentence = full_sentence(2, 'present')
    print(sentence)
    sentence = full_sentence(1, 'future')
    print(sentence)
    sentence = full_sentence(2, 'future')
    print(sentence)


    
    

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "two", "some", "many".
    If quantity == 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "two", "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity == 1, this function will return
            a determiner for a single noun. Otherwise this
            function will return a determiner for a plural noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["two", "some", "many", "the"]

    # Randomly choose and return a determiner.
    #^^^for calling func-- word= get_determiner(2) would make the if statement pull/randomize from else (plural)
    word = random.choice(words)
    # cap_word = word.capitalize(quantity)
    # return cap_word
    return word


def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity == 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    
    noun = random.choice(nouns)

    return noun

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
        ^^ which would be single present (the other being plural present)
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    elif quantity == 1 and tense == "present":
        verbs = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    elif quantity != 1 and tense== "present":
        verbs =["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    elif tense== "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    else:
        verbs ="bomb"

    verb = random.choice(verbs)
    return verb
    
def part_sentence(quantity, tense):
    if quantity == 1:
        word = get_determiner(1)
        noun= get_noun(1)
        verb = get_verb(1, tense)
        p_sentence = f'{word} {noun} {verb} '

        #Make functions plural so that the sentence is plural throughout
        #The elif for the same function but for plural sentence structuring
        
    elif quantity != 1:
        word = get_determiner(2)
        noun = get_noun(2)
        verb = get_verb(2, tense)
        p_sentence = f'{word} {noun} {verb}'
    else:
        p_sentence = "fail"
    return p_sentence

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    preps = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    prep = random.choice(preps)
    return prep

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the determiner
            and noun in the prepositional phrase returned from
            this function are single or pluaral.
    Return: a prepositional phrase.
    """

    #if it is singular (aka =1) then the if statement makes each function singular in their own functions to make a singular prep phrase.
    if quantity == 1:
        prep = get_preposition()
        word = get_determiner(1)
        noun= get_noun(1)
        phrase = prep + ' ' + word + ' ' + noun
        
    # This !=1 makes all functions plural to make a plural prepositional phrase
    elif quantity != 1:
        prep = get_preposition()
        word = get_determiner(2)
        noun = get_noun(2)
        phrase = prep + ' ' + word + ' ' + noun
    return phrase

def full_sentence(quantity, tense):
    if quantity == 1:
        word = get_determiner(1)
        noun= get_noun(1)
        verb = get_verb(1, tense)
        prep = get_prepositional_phrase(1)
        sentence = f'{word} {noun} {verb} {prep}'

        #Make functions plural so that the sentence is plural throughout
        #The elif for the same function but for plural sentence structuring
        
    elif quantity != 1:
        word = get_determiner(2)
        noun = get_noun(2)
        verb = get_verb(2, tense)
        prep = get_prepositional_phrase(2)
        sentence = f'{word} {noun} {verb} {prep}'
    else:
        sentence = "fail"
    return sentence

main()