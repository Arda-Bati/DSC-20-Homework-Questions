
##  DSC 20 HW 09 Solutions  ##

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
    try:

        if not isinstance(input1, int):
            raise TypeError("Inputs are not the correct type")
        if not isinstance(input2, str):
            raise TypeError("Inputs are not the correct type")
        if not isinstance(input3, dict):
            raise TypeError("Inputs are not the correct type")

        return input1 / input3[input2]

    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot divide " + str(input1) + " by " \
+ str(input3[input2]))
    except KeyError:
        raise KeyError("Cannot find " + str(input2) + " in the dictionary")
    except TypeError:
        raise TypeError("Inputs are not the correct type")


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
    try:
        file = open(filename, 'r').readlines()
        return "File loaded"
    except:
        print("Error")
        raise FileNotFoundError(filename + " does not exist")


## Question 3.1 ##

def recursive_triangle(n):
    """
    Creates a triangle structure with * characters. The triangle has n
    levels, each level has one more element than the previous. n is a
    positive integer, no validation is required.
    Parameters: n (int), positive integer
    Returns: triangle string (str)
    Restrictions. You should use recursion in this question.
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
    if n == 1:
        return '*'
    else:
        return recursive_triangle(n - 1) + '\n' + '*' * n


## Question 3.2 ##

def triangle_patterns(n, pattern_count):
    """
    Creates a triangle pattern with * characters. Each triangle has n
    levels, there are pattern_count total triangles. All inputs are
    positive integers, no input validation required.
    Parameters: n, pattern count (int), positive integers
    Returns: triangle string (str)
    Restrictions. You should use recursion in this question.
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
    parity_fac = 2
    if pattern_count == 1:
        return recursive_triangle(n) #First triangle to be printed
    else:
        parity = (pattern_count % 2) * parity_fac - 1
        return triangle_patterns(n, pattern_count - 1) + '\n'\
               + recursive_triangle(n)[::parity]


## Question 4 in Tutor_Fighter.py ##


## Question 5.1 ##

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
    if n == 2:
        return '-' * space_count + 'O' * (n - 1) * 2 + '-' * space_count
    else:
        return full_triangle(n - 1, space_count + 1) + '\n' +\
               '-' * space_count + 'O' * (n - 1) * 2 + '-' * space_count


## Question 5.2 ##

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
    parity_fac = 2
    if pattern_count == 1:
        return full_triangle(n, space_count)
    else:
        parity = (pattern_count % 2) * parity_fac - 1
        return diamond_patterns(n, pattern_count - 1) +\
               '\n' + full_triangle(n, space_count)[::parity]
