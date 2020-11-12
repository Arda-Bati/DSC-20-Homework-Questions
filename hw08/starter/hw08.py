from hw08_data import *

## Question 1 ##

CHECK_OUT = "Checking out book failed"
MEMBER_IN_SYSTEM = "Member already in the library System"
MEMBER_NOT_IN_SYSTEM = "Member is not in the library System"

class Library:
    """
    Library class as explained in HW08 writeup.

    >>> sd = Library("San Diego")
    >>> sd.add_book("Harry Potter")
    >>> sd.get_num_books()
    1
    >>> sd.catalog[0]
    'Harry Potter'
    >>> sd.check_out("Harry Potter")
    >>> sd.get_num_books()
    0
    >>> sd.check_out("Tarzan")
    Checking out book failed
    >>> sd.get_location()
    'San Diego'
    >>> la = Library("Los Angeles")
    >>> la.get_location()
    'Los Angeles'
    >>> la.add_member("Harsh")
    >>> la.add_member("Harsh")
    Member already in the library System
    >>> Library.members[0]
    'Harsh'
    >>> sd.remove_member("Harsh")
    >>> sd.remove_member("Harsh")
    Member is not in the library System
    >>> len(Library.members)
    0
    >>> la.add_member("Brian")

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    """
    ### YOUR CODE GOES HERE ###


class School_Library(Library):
    """
    School_Library class as explained in HW08 writeup. Inherits from the
    Library class. Used specifically for school libraries.

    >>> geisel = School_Library("San Diego", "UCSD")
    >>> geisel.add_member("Harsh")
    >>> geisel.get_school_name()
    'UCSD'
    >>> School_Library.members
    ['Brian', 'Harsh']
    >>> Library.members
    ['Brian', 'Harsh']
    >>> geisel.members
    ['Brian', 'Harsh']

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    """
    ### YOUR CODE GOES HERE ###

## Question 2 ##

class Counter:
    """
    Counter class as explained in HW08 writeup.

    >>> c = Counter("marina langlois")
    >>> print(c.counter_array)
    [3, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 2, 1, 2, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, \
0, 0, 1]
    >>> print(c.get_count(' '))
    1
    >>> print(c.get_count('!'))
    0
    >>> print(c.get_count('m'))
    1

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    """
    ### YOUR CODE GOES HERE ###


## Question 3.1 ##

def street_fighter_champ(tutors):
    """
    Determines the winner of the street fighter championship. The nested list
    'tutors' shows all the matchups.
    Consider tutor tutor1 = ('Dragon', 10, 10)
    tutor1[1] is the skill level
    tutor1[2] is the tie breaker level. In case skills are tied between two
    tutors, the one with the higher tie breaker score wins. If both skill
    level and tie breaker score is the same, the tutor on the left wins.
    Parameters: tutors(list), nested list of lists representing the tournament
    Returns: winner(tuple) The winner of the tournament, in tuple form.
    Restrictions: You should use recursion.

    >>> tutors1 = [Arda]
    >>> tutors2 = [Yuxuan, Arda]
    >>> tutors3 = [[Yuxuan, Arda],[Etsu, Nabi]]
    >>> tutors4 = [[[Yuxuan, Arda],[Etsu, Nabi]],\
[[Wesley, Cecilia],[Aaron, Prem]]]
    >>> tutors5 = [[[[Yuxuan, Arda],[Etsu, Nabi]],\
[[Wesley, Cecilia],[Aaron, Prem]]], [[[Chase, Sudiksha],[Jonathan, Iman]],\
[[Aragorn, Sauron],[Neo, Morpheus]]]]
    >>> street_fighter_champ(tutors1)
    ('Arda', 5, 10)
    >>> street_fighter_champ(tutors2)
    ('Yuxuan', 6, 5)
    >>> street_fighter_champ(tutors3)
    ('Nabi', 7, 5)
    >>> street_fighter_champ(tutors4)
    ('Wesley', 9, 5)
    >>> street_fighter_champ(tutors5)
    ('Neo', 10, 7)

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    """
    ### YOUR CODE GOES HERE ###

## Question 3.2 ##

def street_fighter_detect_spy(tutors):
    """
    Detect the spy from the street fighter tournament. The worst player wins
    the tournament. ie. lower skill player always wins any matchup. In case of
    skill tie, lower tie breaker score always wins. In case of ties in both,
    the tutor on the right wins.
    Parameters: tutors(list), nested list of lists representing the tournament
    Returns: spy(str) The absolute loser of the tournament, in string form.
    Restrictions: You should use recursion.

    >>> tutors0 = [('Pla3', 4, 1)]
    >>> tutors1 = [[('Pla2', 6, 5), ('Pla1', 5, 10)],[('Pla3', 4, 1),\
('Pla4', 4, 2)]]
    >>> tutors2 = [[[('Pla2', 6, 5), ('Pla1', 5, 10)],[('Pla3', 4, 1),\
('Pla4', 4, 2)]], [[('Pla5', 9, 5), ('Pla8', 8, 3)],[('Pla6', 7, 10),\
('Pla7', 8, 5)]]]
    >>> street_fighter_detect_spy(tutors0)
    'Etsu'
    >>> street_fighter_detect_spy(tutors1)
    'Etsu'
    >>> street_fighter_detect_spy(tutors2)
    'Etsu'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    """
    ### YOUR CODE GOES HERE ###


## Question 4 ##

def make_reviews_list(dining_hall, ratings):
    """
    Creates a list of reviews for a particular dining hall given a list of
    ratings.

    Try using list comprehesions!

    >>> make_reviews_list('A', [123])
    [['A', 123]]
    >>> make_reviews_list('B', [0, 1])
    [['B', 0], ['B', 1]]
    >>> make_reviews_list('7th College Dining Hall', [])
    []
    >>> make_reviews_list('Foodworx', ["Best food", 5, ":)", 100, 1, 1, 5])
    [['Foodworx', 'Best food'], ['Foodworx', 5], ['Foodworx', ':)'], \
['Foodworx', 100], ['Foodworx', 1], ['Foodworx', 1], ['Foodworx', 5]]

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    """
    ### YOUR CODE GOES HERE ###


## Question 5 ##

def average_rating(dining_hall, reviews=google_reviews):
    """
    Finds the average rating for a particular dining hall. The list of
    reviews is given as the second parameter. The average rating should be
    returned as its own review.

    >>> average_rating('Canyon Vista')
    2.2
    >>> average_rating('64 Degrees')
    4.2
    >>> average_rating('Foodworx')
    3.4
    >>> average_rating('Pines')
    3.6

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    """
    ### YOUR CODE GOES HERE ###


## Question 6 ##

def better_dining_hall(first, second):
    """
    Returns the name of the better dining hall between the two given
    dining halls. The better dining hall is the dining hall with a higher
    average review.

    >>> better_dining_hall('OVT', 'Pines')
    'OVT'
    >>> better_dining_hall('Canyon Vista', 'Pines')
    'Pines'
    >>> better_dining_hall('Cafe Ventanas', '64 Degrees')
    '64 Degrees'
    >>> better_dining_hall('64 Degrees', 'OVT')
    '64 Degrees'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    """
    ### YOUR CODE GOES HERE ###
