"""
DSC 20 HW 03
NAME:
PID:
"""

from math import isclose

## Question 1 ##

def order_scores(student_ids, student_scores, student_hours_worked):
    """
    Orders elements of student_ids, student_scores, and student_hours_worked,
    according to the contents of student_scores (descending order)

    >>> order_scores(['Work','Hard','Get','A'],[100, 80, 90, 70],[10,12,13,10])
    {'Work': (100, 10), 'Get': (90, 13), 'Hard': (80, 12), 'A': (70, 10)}
    >>> order_scores(['A1','A2','A3'],[90, 27, 56],[9,10, 6])
    {'A1': (90, 9), 'A3': (56, 6), 'A2': (27, 10)}
    >>> order_scores(['A1','A2','A3'],[90.4, 27],[9,10, 6])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> order_scores(['A1','A2','A3'],[90, 27, 80],[9,10, "hello!!"])
    Traceback (most recent call last):
    ...
    AssertionError
    """

## Question 2 ##

def counting_spaces(list_of_strings):
    """
    >>> test = ["s t r i n g ", 'nospace', 'one space']
    >>> counting_spaces(test)
    [True, True, 1]

    >>> test2 = ["two spac es", "thr ee spa ces", "nospaces"]
    >>> counting_spaces(test2)
    [2, True, True]

    """

## Question 3 ##

def create_trigrams(input_file, starting_words, num_words):
    """read in the input text, create a dictionary of trigrams, generate
    a new story based on the sequence of words starting a pair of words

    >>> create_trigrams("data/sherlock_small.txt", "one night", 10)
    'one night it was on the twentieth of march 1888'

    >>> create_trigrams("data/sherlock_small.txt", "i was", 10)
    'i was returning from a journey to a patient for'

    >>> create_trigrams("data/sherlock_small.txt", "Holmes Sherlock", 10)
    Traceback (most recent call last):
    ...
    AssertionError
    """

## Question 4 ##

DELTA = 0.0001

def newton_sqrt(n):
    """
    >>> newton_sqrt(4)
    1
    >>> newton_sqrt(1)
    5
    >>> newton_sqrt(2)
    4
    """

## Question 5.1 ##

B = 'O'
W = ' '

def list_to_pixel(file_path, filename):
    """
    >>> list_to_pixel("data/list0.txt","graph.txt")
    >>> with open ("graph.txt", "r") as f:
    ...     print(f.readline())
      OOOO
    <BLANKLINE>
    """


## Question 5.2 ##

def pixel_to_list(pixel):
    """
    >>> pixel0="O OO OOOO OO O\\n"
    >>> pixel_to_list(pixel0)
    [[0, 1, 1, 2, 1, 4, 1, 2, 1, 1]]


    >>> with open("data/pixel_art.txt",'r') as infile:
    ...     pixel1 = infile.readlines()
    >>> pixel1 = ''.join(pixel1)
    >>> pixel_to_list(pixel1)
    [[2, 4, 2], [1, 2, 2, 2, 1], [0, 2, 4, 2], [0, 1, 6, 1], \
[0, 1, 6, 1], [0, 2, 4, 2], [1, 2, 2, 2, 1], [2, 4, 2]]
    """

## Question 6 Extra Credit ##

def parameter_debugger(*params):
    """
    Given a list of string values representing function parameter, output a
    tuple with two items: a corrected list of parameter and a boolean value
    telling whether the list has been corrected or not.

    >>> parameter_debugger('first', 'second=30', '*third', '**fourth')
    (['first', 'second=30', '*third', '**fourth'], True)
    >>> parameter_debugger('slope', '*constants', 'intercept')
    (['slope', 'intercept', '*constants'], False)
    >>> parameter_debugger('*tutor', 'professor="Marina"', '*ta', 'me')
    (['me', 'professor="Marina"', '*tutor'], False)
    """
