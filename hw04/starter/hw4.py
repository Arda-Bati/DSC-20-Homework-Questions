"""
DSC 20 HW 04
NAME:
PID:
"""

from math import factorial
from math import floor

## Question 1 ##  (Checkpoint Question)
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

## Question 2.1 ##  (Checkpoint Question)
def exp_gen(n, e):
    """A generator that yields the following exponentials
    (given n, e as inputs):
    n**e, (n*e)**e, (n*e*e)**e, (n*e*e*e)**e, ... (and so on)
    >>> gen = exp_gen(2,2)
    >>> next(gen)
    4
    >>> next(gen)
    16
    >>> next(gen)
    64
    >>> next(gen)
    256
    """

## Question 2.2 ##  (Checkpoint Question)
def luc_seq():
    """A generator that yields the Lucas Sequence
    >>> gen = luc_seq()
    >>> next(gen)
    2
    >>> next(gen)
    1
    >>> next(gen)
    3
    """

## Question 2.3 ##  (Checkpoint Question)
def alpha_gen(stars_count, word):
    """Return a function that creates a generator that yields a
    letter from a given string with a specified number of stars between
    each letter.

    >>> alpha_gen = alpha_gen(2, "marina")
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


## Question 2.4 ##  (Checkpoint Question)
def generate_generators():
    """
    Return a generator that yields the previous three generators.
    First Yield:  exp_gen
    Second Yield: luc_seq
    Third Yield:  alpha_gen

    >>> gen_list = generate_generators()
    >>> exp_gnr = next(gen_list)
    >>> lucas_gnr = next(gen_list)
    >>> alpha_func = next(gen_list)
    >>> func1 = exp_gnr(2,2)
    >>> next(func1)
    4
    >>> next(func1)
    16
    >>> next(func1)
    64
    >>> next(lucas_gnr)
    2
    >>> next(lucas_gnr)
    1
    >>> next(lucas_gnr)
    3
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

    >>> subLsts = [[1, 5, 2, 8, 4], [-900, -22, 33, -90, 529],\
[0, -2, 5, -199, 300]]
    >>> isinstance(type(get_negative_lists(subLsts)), type(map))
    True
    >>> list(get_negative_lists(subLsts))
    [[-900, -22, 33, -90, 529], [0, -2, 5, -199, 300]]
    >>> subLsts = [[7, 2, -1, -6, -100], [-1, 0, 5, 2, 3], [0, 0, 1, 0, 0]]
    >>> list(get_negative_lists(subLsts))
    [[7, 2, -1, -6, -100], [-1, 0, 5, 2, 3]]
    """

## Question 4 ##
def get_distances():
    """
    Return a list of lambdas that help do bulk distance calculations on city
    coordinates.
    1: Define a function that converts miles to km, with miles as the input.
    2: Define a function that determines the distance between two points that
       use (x, y) coordinates as inputs
    3: Determine how many kilometers are between Point A(424.3601, 71.0589)
       and Point B (-3601.1128, 493.4276)
    4: Return a lambda that returns a map object of the distances between a
       list of tuple pairs of cities.


    >>> cities = [(424.3601, 71.0589), (-3601.1128, 493.4276), \
(158.1010, 8179.001), (-119.030, -117.334)]
    >>> lambda_functions = get_distances()
    >>> lambda_functions[0](1000)
    1609.344
    >>> lambda_functions[1](cities[0][0], cities[0][1],\
cities[1][0], cities[1][1])
    4047.5705537240606
    >>> lambda_functions[2]((cities[0], cities[1]))
    6513.933385212495
    >>> list(lambda_functions[3]([(cities[0], cities[1]),\
(cities[2], cities[3])]))
    [6513.933385212495, 13359.103960657963]
    """

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

## Question 7 ## (Extra Credit)
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
