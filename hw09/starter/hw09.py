"""
Homework 9 questions Q1, Q2, Q3, Q5
"""

## Question 1 ##

def checkingInputs(input1, input2, input3):
    """
    You will be handling 3 basic checks
    - are all the input types correct
    - does input2 exist within input3
    - can you divide input1 by input3

    >>> checkingInputs(15, 'key1', {'key1': 5, 'key2': 10})
    3.0

    >>> checkingInputs(15, 'key1', {'key1': 0, 'key2': 10})
    Traceback (most recent call last):
    ...
    ZeroDivisionError: Cannot divide 15 by 0

    >>> checkingInputs(15, 'key1', {'key2': 10})
    Traceback (most recent call last):
    ...
    KeyError: 'Cannot find key1 in the dictionary'

    >>> checkingInputs("15", 2810, ['key2', 10])
    Traceback (most recent call last):
    ...
    TypeError: Inputs are not the correct type

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    """
    ## YOUR CODE IS HERE ##


## Question 2 ##

def loadFile(filename):
    """
    >>> loadFile("file1.txt")
    'File loaded'

    >>> loadFile("file2.txt")
    Traceback (most recent call last):
        ...
    FileNotFoundError: file2.txt does not exist

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    """
    ## YOUR CODE IS HERE ##


## Question 3.1 ##

def recursive_triangle(n):
    """
    Creates a triangle structure with * characters. The triangle has n
    levels, each level has one more element than the previous. n is a
    positive integer, no validation is required.
    Parameters: n (int), positive integer
    Returns: triangle string (str)
    Restrictions. This function should be recursive.
    >>> print(recursive_triangle(1))
    *
    >>> print(recursive_triangle(2))
    *
    **
    >>> print(recursive_triangle(3))
    *
    **
    ***

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    """
    ## YOUR CODE IS HERE ##


## Question 3.2 ##

def triangle_patterns(n, pattern_count):
    """
    Creates a triangle pattern with * characters. Each triangle has n
    levels, there are pattern_count total triangles. All inputs are
    positive integers, no input validation required.
    Parameters: n, pattern count (int), positive integers
    Returns: triangle string (str)
    Restrictions. This function should be recursive.
    >>> print(triangle_patterns(3, 1))
    *
    **
    ***
    >>> print(triangle_patterns(3, 2))
    *
    **
    ***
    ***
    **
    *
    >>> triangle_patterns(3, 3)
    '*\\n**\\n***\\n***\\n**\\n*\\n*\\n**\\n***'
    >>> triangle_patterns(3, 4)
    '*\\n**\\n***\\n***\\n**\\n*\\n*\\n**\\n***\\n***\\n**\\n*'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    """
    ## YOUR CODE IS HERE ##


## Question 4 ##

## This question's implementation will be done in the Tutor_Fighter.py file.


## Question 5.1 (EXTRA CREDIT) ##

def full_triangle(n, space_count = 0):
    """
    Creates a triangle structure as shown in the doctests. The triangles has
    n - 1 levels. space_count is a helper variable used to help with spacing
    of the triangle. Assume n >= 2, and space_count >= 0. All inputs are
    integers. No input validation is required.
    Parameters: n, space count (int), integers. n >= 1, space_count >= 0.
    Returns: triangle string (str)
    Restrictions. You should use recursion in this question.
    >>> print(full_triangle(2)) # The smallest value we can have
    OO
    >>> print(full_triangle(3))
    -OO-
    OOOO
    >>> print(full_triangle(5))
    ---OO---
    --OOOO--
    -OOOOOO-
    OOOOOOOO
    >>> full_triangle(6)
    '----OO----\\n---OOOO---\\n--OOOOOO--\\n-OOOOOOOO-\\nOOOOOOOOOO'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    """
    ## YOUR CODE IS HERE ##


## Question 5.2 (EXTRA CREDIT) ##

def diamond_patterns(n, pattern_count, space_count = 0):
    """
    Assume n >= 2, pattern_count >= 1 and space_count >= 0. All inputs are
    integers. No assertion required.
    >>> print(diamond_patterns(2,1))
    OO
    >>> print(diamond_patterns(2,2))
    OO
    OO
    >>> print(diamond_patterns(5,1))
    ---OO---
    --OOOO--
    -OOOOOO-
    OOOOOOOO
    >>> diamond_patterns(4,2)
    '--OO--\\n-OOOO-\\nOOOOOO\\nOOOOOO\\n-OOOO-\\n--OO--'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    """
    ## YOUR CODE IS HERE ##
