"""
DSC 20 HW 04
NAME:
PID:
"""

from math import factorial
from math import floor

## Question 1 ##
def prime_number_generator(number_of_primes):
    """
    Generator for creating the first 'number_of_primes' prime numbers
    using the prime number formula based on Wilson's theorem

    Restrictions:
    You should use a generator in this question.

    Parameters:
    number_of_primes (int): Number of primes to be generated

    Returns:
    The required generator of the question.

    >>> prime_gen = prime_number_generator(2)
    >>> next(prime_gen)
    2
    >>> list(prime_number_generator(10))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    >>> prime_gen = prime_number_generator(20)
    >>> list(prime_gen)[10:20]
    [31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    """

    primes_count = 0 #number of prime numbers generated so far
    offset = 2       #offset for the prime number formula
    cur_integer = 1   #current integer being used in the formula

    while primes_count < number_of_primes:

        n_fact = factorial(cur_integer)
        is_prime = (n_fact % (cur_integer+1)) // cur_integer

        if(is_prime):
            primes_count += 1
            yield is_prime * (cur_integer-1) + offset

        cur_integer += 1

## Question 2 ##
def generate_generators():
    """
    Return a generator that yields the following generators:
    On the first yield the function should return:
        A generator that yields the following exponentials (given n, e as inputs):
        n**e, (n*e)**e, (n*e*e)**e, (n*e*e*e)**e, ... (and so on)
    Second yield:
       A generator for the Lucas Sequence.
        f(n) = f(n-1) + f(n-2), where f(0) = 2 and f(1) = 1
    Third Yield:
        A function that returns a generator for each element in the alphabet
        with a space_count number of spaces between each letter.

    >>> gen_list = generate_generators()
    >>> exp_gen = next(gen_list)
    >>> lucas_gen = next(gen_list)
    >>> alpha_func = next(gen_list)
    >>> func1 = exp_gen(2,2)
    >>> next(func1)
    4
    >>> next(func1)
    16
    >>> next(lucas_gen)
    2
    >>> next(func1)
    64
    >>> next(lucas_gen)
    1
    >>> alpha_gen = alpha_func(2, "marina")
    >>> next(alpha_gen)
    'm'
    >>> next(alpha_gen)
    '*'
    >>> next(alpha_gen)
    '*'
    >>> for i in alpha_gen:
    ... 	print(i, end='')
    a**r**i**n**a**
    """
    # Return an exponential generator
    def exp_gen(n, e):
        while True:
            yield n**e
            n *= e

    # Lucas Sequence f(n) = f(n-1) + f(n-2), where f(0) = 2 and f(1) = 1
    def luc_seq():
        a, b = 2, 1
        while True:
            yield a
            a, b = b, a + b

 	# Creates a generator that yields a letter from a given string with a
    # specified number of stars between each letter.
    def alpha_gen(stars_count, word):
        for letter in word:
            yield letter
            for i in range(stars_count):
                yield '*'

    generators = [exp_gen, luc_seq(), alpha_gen]
    return (i for i in generators)

## Question 3 ##
def get_negative_lists(super_list):
    """
    Return a map object containing the lists in the
    super list that contain negative numbers.

    Restrictions:
    No loops (Not even list comprehension!)

    Parameters:
    super_list (list): A list containing sublists of integers

    Returns:
    The map required by the question.

    >>> subLsts = [[1, 5, 2, 8, 4], [-900, -22, 33, -90, 529], \
    [0, -2, 5, -199, 300]]
    >>> isinstance(type(get_negative_lists(subLsts)), type(map))
    True
    >>> list(get_negative_lists(subLsts))
    [[-900, -22, 33, -90, 529], [0, -2, 5, -199, 300]]
    >>> subLsts = [[7, 2, -1, -6, -100], [-1, 0, 5, 2, 3], [0, 0, 1, 0, 0]]
    >>> list(get_negative_lists(subLsts))
    [[7, 2, -1, -6, -100], [-1, 0, 5, 2, 3]]
    """
    bools = map(lambda lst: (lst, list(map(lambda val:val >= 0, lst))),\
                super_list)
    filtered_lsts = filter(lambda sublist: False in sublist[1], bools)

    return map(lambda sublist: sublist[0], filtered_lsts)

## Question 4 ##
def get_distances():
    """
    Return a list of lambdas that help do bulk distance calculations on city
    coordinates.
        1: Define a function that converts between miles and km, with miles as
           the input.
        2: Define a function that determines the distance between two points
           that use (x, y) coordinates as inputs
        3: Determine how many kilometers are between Point A (424.3601,71.0589)
           and Point B (-3601.1128, 493.4276)
        4: Return a lambda that returns a map object of the distances between a
           list of tuple pairs of cities.


    >>> cities = [(424.3601, 71.0589), (-3601.1128, 493.4276), \
                  (158.1010, 8179.001), (-119.030, -117.334)]
    >>> lambda_functions = get_distances()
    >>> lambda_functions[0](1000)
    1609.344
    >>> lambda_functions[1](cities[0][0], cities[0][1], cities[1][0],\
                            cities[1][1])
    4047.5705537240606
    >>> lambda_functions[2]((cities[0], cities[1]))
    6513.933385212495
    >>> list(lambda_functions[3]([(cities[0], cities[1]), (cities[2],\
             cities[3])]))
    [6513.933385212495, 13359.103960657963]
    """
    # Q1 Define a function that converts between miles and km,
    # with miles as the input.
    conv_var = 1.609344
    miles_convert_func = lambda miles:conv_var * miles
    # Q2 Define a function that determines the distance between two points
    # using two (x, y) coordinates as tuple inputs
    dist_func = lambda x1, y1, x2, y2:((y2-y1)**2 + (x2-x1)**2)**(1/2)
    # Q3 Determine how many kilometers are between
    # Point A (424.3601, 71.0589) and Point B (-3601.1128, 493.4276)
    km_dist_combined = lambda cities:miles_convert_func(dist_func(
        cities[0][0], cities[0][1], cities[1][0], cities[1][1]))
    # Q4 Return a lambda that determines distances between a list
    # of tuple pairs of cities.
    bulk_dist_compute = lambda cty_lst:map(km_dist_combined, cty_lst)

    return [miles_convert_func, dist_func, km_dist_combined, bulk_dist_compute]

## Question 5 ##
def calculate_wages(filepath):
    """
    Calculator for tutor wages. See question description for explanation.

    Restrictions:
    No loops (Not even list comprehension!)

    Parameters:
    filepath (str): Path to the input file

    Returns:
    dict: Dictionary of tutor names and their total wages

    >>> calculate_wages('data/input.txt')
    {'Nabi': 8, 'Arda': 40, 'K': 460}
    """

    with open('data/input.txt', 'r') as f:
        content = f.read()
        lines = content.strip().split('\n')
        names_and_weeks = map(lambda x: x.split(', '), lines)
        names_and_weeks = map(lambda x: (x[0], map(lambda x: int(x), x[1:])),\
                              names_and_weeks)
        names_and_wages = map(lambda x: (x[0], map(lambda y:\
                              max(min((y-5)*8, 5*8),0) + max((y-10)*12, 0),\
                              x[1])), names_and_weeks)
        names_and_wages = map(lambda x: (x[0], sum(x[1])),names_and_wages)
        return dict(names_and_wages)


## Question 6 ##
def calculate_best_scores(formulas, scores):
    """
    Calculates the maximum score achievable with the provided formulas.

    Restrictions:
    No loops (Not even list comprehension!)

    Parameters:
    formulas (list(lambda)) : List of lambda functions to be applied to scores
    scores (list(int)) : List of integers indicating the scores for students

    Returns:
    list : List of scores with the function that maximizes each score applied
    to it

    >>> calculate_best_scores([lambda x : x - 1], [3, 4, 5])
    [3, 4, 5]
    >>> calculate_best_scores([lambda x : x + 1], [3, 4, 5])
    [4, 5, 6]
    >>> calculate_best_scores([lambda x : x + 1, lambda x : x * 2,\
lambda x : x - 1], [3, 4, 5])
    [6, 8, 10]
    >>> calculate_best_scores([lambda x : x + 20, lambda x : x * 2,\
lambda x : x * 3], [3, 4, 20])
    [23, 24, 60]
    >>> calculate_best_scores([lambda x : x + 20, 123], [3, 4, 5])
    [23, 24, 25]

    """
    check_type_lst = list(map(lambda x:isinstance(x, int), scores))
    assert False not in check_type_lst, "Scores list must only contain valid numbers."
    assert isinstance(formulas, list), "Formulas input must be a list."
    assert isinstance(scores, list), "Scores input must be a list."

    formulas += [lambda x : x] # To assure grades are not getting lowered
    increasing_functions = list(filter(lambda func : callable(func), formulas))
    best_scores = map(lambda score: max(map(lambda func: func(score),\
                      increasing_functions)), scores)
    return list(best_scores)

## Question 7 ##

def find_positive_magic_integer(filepath):
    """
    Find any positive magic integers in the given file and output a dictionary
    whose keys are the string value of the found magic numbers and values
    are the line numbers where they were found.

    Parameters:
    filepath (str): A string containing the filepath.

    Returns:
    The dictionary described above.

    >>> find_positive_magic_integer('./data/magic_number_test1.py')
    {'2': [3, 11], '3': [4, 11], '4': [5, 11], '5': [6, 11], '6': [7, 11], \
'7': [8, 11], '8': [9, 11], '9': [10, 11]}
    >>> find_positive_magic_integer('./data/magic_number_test2.py')
    {'2': [4, 5], '3': [4, 6], '20': [7], '5': [8]}
    """

    magic_number_dict = {}

    # constants
    NON_MAGIC_NUMBERS = ['-1', '0', '1']
    # variable declaration related constants
    NUMBER_OF_ELEMENT_IN_DECLARATION = 3
    EQUAL_SIGN_POS_IN_DECLARATION = 1
    NUMBER_POS_IN_DECLARATION = 2

    with open(filepath, "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            # separate the line into chunks of string separated by whitespace
            elements = lines[i][:-1].split(" ") \
                if lines[i][-1] == '\n' else lines[i].split(" ")

            # check if is a variable declaration statement
            if len(elements) == NUMBER_OF_ELEMENT_IN_DECLARATION \
                    and elements[EQUAL_SIGN_POS_IN_DECLARATION] == "=" \
                    and elements[NUMBER_POS_IN_DECLARATION].isnumeric():
                continue

            for e in elements:
                if e.isnumeric() and e not in NON_MAGIC_NUMBERS:
                    if e not in magic_number_dict:
                        magic_number_dict[e] = []
                    line_number = i + 1
                    if (line_number) not in magic_number_dict[e]:
                        magic_number_dict[e].append(line_number)

    return magic_number_dict
