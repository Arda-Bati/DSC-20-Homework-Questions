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
    assert isinstance(student_ids, list) & isinstance(student_scores, list)& \
    isinstance(student_hours_worked, list)
    assert len(student_ids) == len(student_scores) == len(student_hours_worked)

    assert all(isinstance(element, str) for element in student_ids)
    assert all(isinstance(element, int) for element in student_scores)
    assert all(isinstance(element, int) for element in student_hours_worked)

    if len(student_ids) == 0:
        return dict()

    lists_zipped = list(zip(student_scores, student_ids, student_hours_worked))
    lists_zipped.sort(reverse=True)

    student_info = dict()

    for student in lists_zipped:
        student_info.update({student[1]: (student[0], student[2])})

    return student_info

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
    assert type(list_of_strings) == list
    assert all(isinstance(element, str) for element in list_of_strings)

    return [True if x.count(" ") % 3 == 0 else x.count(" ") for x in list_of_strings]

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
    assert type(input_file) == str
    assert type(starting_words) == str
    assert type(num_words) == int

    with open(input_file, 'r') as file:
        data = file.read().replace('\n', '')
        data = data.lower()
        data = data.split()

    trigrams = {}

    for i in range(len(data)-2):
        trigrams[data[i] + " " + data[i+1]] = data[i+2]

    assert starting_words in trigrams

    result = starting_words.split()
    current = starting_words

    for i in range(num_words-2):
        if current in trigrams:
            result.append(trigrams[current])
            current = " ".join(result[-2:])
    return " ".join(result)


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
    i = 1
    x = n/2
    while True:
        if isclose(x**2, n, abs_tol=DELTA):
            break
        x=(x+n/x)/2
        i+=1
    return i


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
    with open(file_path, 'r') as infile:
        lines = infile.readlines()
    lst = [[int(val) for val in line.rstrip('\n').split(',') if val] for line in lines if line]

    to_save = ''
    for row in lst:
        for ix in range(len(row)):
            # even index codes for white
            if ix%2 == 0:
                to_save += W*row[ix]
            else:
                to_save += B*row[ix]
        to_save += '\n'

    with open(filename,'w') as outfile:
        outfile.write(to_save)

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
    lst=[]
    if pixel == '': return lst
    pixel = pixel.rstrip('\n').split('\n')

    for line in pixel:
        row = []
        white = 0
        black = 0

        # 0 encodes for white and 1 encodes for black
        prev = 0
        for p in line:
            # check if current pixel is white
            if not prev:
                if p == W:
                    white += 1
                else:
                    row.append(white)
                    white = 0
                    black += 1
                    prev = 1
            else:
                if p == B:
                    black += 1
                else:
                    row.append(black)
                    black = 0
                    white += 1
                    prev = 0

        row.append(white or black)
        lst.append(row)

    return lst

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

    normal, default, args, kwargs = [], [], [], []
    for p in params:
        if "**" in p:
            kwargs += [p]
        elif "*" in p:
            args += [p]
        elif "=" in p:
            default += [p]
        else:
            normal += [p]

    # combine each param type in the correct order
    out_params = normal + default + args[:1] + kwargs[:1]
    # check if the input params were correct or not
    was_correct = True
    if len(args) > 1 or len(kwargs) > 1 \
            or sum([i != j for i,j in zip(params, out_params)]) > 0:
        was_correct = False

    return out_params, was_correct
