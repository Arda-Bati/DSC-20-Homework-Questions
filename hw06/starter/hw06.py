"""
DSC 20 HW 06
NAME:
PID:
"""

## Question 1.1 ##
def conversion_binary(n):
    """
    Converts the given base-10 number to binary representation.

    Restrictions:
    You should use recursion in this question. You should do input validation.

    Parameters:
    n (int): Number to convert

    Returns:
    (str): Binary representation of the input

    >>> conversion_binary(86)
    '1010110'
    >>> conversion_binary(1)
    '1'
    >>> conversion_binary(0)
    '0'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++

    """

## Question 1.2 ##
def conversion_any(n, base):
    """
    Converts the given base-10 number to any base representation given by the
    base parameter. Assume that base will be 10 maximum.

    Restrictions:
    You should use recursion in this question. You should do input validation.

    Parameters:
    n (int): Number to convert
    base (int): Base to convert the number to

    Returns:
    (str): Base-x representation of the input number n

    >>> conversion_any(86, 2)
    '1010110'
    >>> conversion_any(86, 3)
    '10012'
    >>> conversion_any(86, 4)
    '1112'
    >>> conversion_any(86, 10)
    '86'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++

    """

## Question 2.1 ##
def create_recursive_list(rec_count):
    """
    Returns a list with a recursive structure who has "rec_count" levels.

    Restrictions:
    You should use recursion in this question. You should do input validation.

    Parameters:
    rec_count (int): Depth of recursion in the list

    Returns:
    Recursion list specified in the question

    >>> create_recursive_list(0)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> create_recursive_list(1)
    [1]
    >>> create_recursive_list(2)
    [2, [1]]
    >>> create_recursive_list(5)
    [5, [4, [3, [2, [1]]]]]

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++

    """

## Question 2.2 ##
def decode_recursive_list(rec_list):
    """
    Decodes a list of the recursive structure from the previous question.
    Returns a single level list containing the elements of the above list,
    in the same order.

    Restrictions:
    You should do input validation.

    Parameters:
    rec_list (list): Recursive list as defined in Q1.1

    Returns:
    Recursive list decoded in a normal list format

    >>> decode_recursive_list([1])
    [1]
    >>> decode_recursive_list([2, [1]])
    [2, 1]
    >>> decode_recursive_list([5, [4, [3, [2, [1]]]]])
    [5, 4, 3, 2, 1]

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++

    """

## Question 3.1 ##
def fibonacci_gen():
    """
    Yields the numbers of the Fibonacci sequence starting from F(1).

    Restrictions:
    This function should be a generator

    Returns:
    The fibonacci sequence in generator format

    >>> fibo = fibonacci_gen()
    >>> next(fibo)
    1
    >>> next(fibo)
    1
    >>> [next(fibo) for i in range(8)]
    [2, 3, 5, 8, 13, 21, 34, 55]

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++

    """

## Question 3.2 ##
def approximate_pi(n):
    """
    Returns  the nth approximation of pi according to the Leibniz series.

    Restrictions:
    You should do input validation. You should round results to the 3rd
    decimal place. You should use recursion in this question.

    Parameters:
    n (int): Represents nth approximation of pi.

    Returns:
    (float) The nth approximation of pi.

    >>> approximate_pi(1)
    4
    >>> approximate_pi(25)
    3.181
    >>> approximate_pi(50)
    3.122

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++

    """

## Question 3.3 ##
def pi_fibo_generator():
    """
    Yields the result of the current approximation of pi times the
    the current fibonacci number in their respective sequences.

    Restrictions:
    You should do input validation. You should round results to the 3rd
    decimal place.

    Returns:
    Multiplication of the nth approximation of pi and nth fibonacci number

    >>> pi_fibo = pi_fibo_generator()
    >>> [next(pi_fibo) for i in range(5)]
    [4, 2.667, 6.934, 8.688, 16.7]
    >>> [next(pi_fibo) for i in range(5)]
    [23.808, 42.692, 63.357, 110.568, 167.255]
    >>> [next(pi_fibo) for i in range(5)]
    [287.559, 440.208, 749.561, 1157.013, 1956.27]

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++

    """

## Question 4 ##
def create_powerset(parent_list):
    """
    Creates the powerset of the set represented by parent_list.

    Restrictions:
    You should do input validation. You can use at most one loop (not nested).

    Parameters:
    parent_list (list): The list for which the powersets will be created

    Returns:
    (list) The powerset of list parent_list

    >>> create_powerset([])
    [[]]
    >>> create_powerset('hello')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> lst_to_return = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    >>> arg1 = create_powerset([1, 2, 3])
    >>> arg1.sort()
    >>> arg1 == lst_to_return
    True

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    """

## Question 5.1 ##
def recursive_reverse_up_to_n(name, n):
    """
    Recursively reverses the given string at chunks 1..n

    Restrictions:
    You should use recursion. You should do input validation.

    Parameters:
    name (str): The string to be reversed
    n (int): How many times the string should be reversed

    Returns:
    (str) Reversed string with the given formula

    >>> recursive_reverse_up_to_n('Nabi', 3)
    'bNai'
    >>> recursive_reverse_up_to_n('klmn', 3)
    'mkln'
    >>> recursive_reverse_up_to_n('klmn', 4)
    'nlkm'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++

    """

## Question 5.2 ##
def undo_recursive_reverse_up_to_n(name, n):
    """
    Recursively corrects the recursive reverse
    done on the string up to n characters.

    Restrictions:
    You should use recursion. You should do input validation.

    Parameters:
    name (str): The string to be corrected
    n (int): How many times the string has been previously reversed

    Returns:
    (str) Corrected string

    Parameters:
    name (str): The string to be corrected
    n (int): How many times the string has been previously reversed

    Returns:
    (str) Corrected string

    >>> undo_recursive_reverse_up_to_n('bNai', 3)
    'Nabi'
    >>> undo_recursive_reverse_up_to_n('mkln', 3)
    'klmn'
    >>> undo_recursive_reverse_up_to_n('nlkm', 4)
    'klmn'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++

    """

## Question 6 ##
def build_repr(operations, templates):
    """
    Build the representation of the series of operations with the given
    templates. The operations are prioritized from right to left.

    Restrictions:
    You should use recursion. You should do input validation.

    Parameters: operations (list(str)): List of numbers and operations to be
    executed on them

    Returns: (str): String representation of the operations

    >>> build_repr([0, '+', 1, '-', 3], {'+': '({0}, +, {1})', '-':\
    '({0}, -, {1})'})
    '(0, +, (1, -, 3))'

    >>> build_repr([0, '+', 1, '-', 3], \
    {'+': '({0}, add, {1})', '-':'({0}, minus, {1})'})
    '(0, add, (1, minus, 3))'

    >>> build_repr([0, '+', 1, '-', 3], \
    {'+': '({0}, add, {1})', '-': '({0}, minus, {1})'})
    '(0, add, (1, minus, 3))'

    ++++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW:
    ++++++++++++++++++++++++++

    """
