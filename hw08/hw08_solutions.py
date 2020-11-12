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

    #keeps track of members across all libraries
    members = []

    def __init__(self, location):
        self.location = location
        self.catalog = []

    def add_book(self, book):
        self.catalog.append(book)

    def check_out(self, book):
        if book in self.catalog:
            self.catalog.remove(book)
        else:
            print(CHECK_OUT)

    def get_location(self):
        return self.location

    def get_num_books(self):
        return len(self.catalog)

    def add_member(self, member):
        if member in Library.members:
            print(MEMBER_IN_SYSTEM)
        else:
            Library.members.append(member)

    def remove_member(self, member):
        if member in Library.members:
            Library.members.remove(member)
        else:
            print(MEMBER_NOT_IN_SYSTEM)


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

    def __init__(self, location, school_name):
        Library.__init__(self, location)
        self.school_name = school_name

    def get_school_name(self):
        return self.school_name

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

    def __init__(self, string):
        self.counter_array = Counter.count_us(string)

    def count_us(string):
        l = [0] * 27
        for c in string:
            if c == ' ':
                l[len(l) - 1] = l[len(l) - 1] + 1
            else:
                value = ord(c)
                index = value - 97
                l[index] = l[index] + 1
        return l

    def get_count(self, character):
        if character == " ":
            return self.counter_array[len(self.counter_array)-1]
        value = ord(character)
        index = value - 97
        if 0<= index <=len(self.counter_array):
            return self.counter_array[index]
        else:
            return 0


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

    if len(tutors) == 1 or isinstance(tutors, tuple):
        if isinstance(tutors, list):
            return tutors[0]
        return tutors

    tutor1 = street_fighter_champ(tutors[0])
    tutor2 = street_fighter_champ(tutors[1])

    if tutor1[1] > tutor2[1]:
        return tutor1
    elif tutor1[1] < tutor2[1]:
        return tutor2
    else:
        if tutor1[2] >= tutor2[2]:
            return tutor1
        else:
            return tutor2

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

    if len(tutors) == 1 or isinstance(tutors, tuple):
        if isinstance(tutors, list): # list
            tutor_id = tutors[0][0]
            tutor_name = secret_dict[tutor_id]
            return tutor_name
        else: # tuple
            tutor_id = tutors[0]
            tutor_name = secret_dict[tutor_id]
            return tutor_name

    tutor1_name = street_fighter_detect_spy(tutors[0])
    tutor2_name = street_fighter_detect_spy(tutors[1])
    tutor1 = secret_dict[tutor1_name]
    tutor2 = secret_dict[tutor2_name]

    if tutor1[1] < tutor2[1]:
        return secret_dict[tutor1[0]]
    elif tutor1[1] > tutor2[1]:
        return secret_dict[tutor2[0]]
    else:
        if tutor1[2] < tutor2[2]:
            return secret_dict[tutor1[0]]
        else:
            return secret_dict[tutor2[0]]


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

    list = []
    for i in range(len(ratings)):
        review = make_review(dining_hall, ratings[i])
        list.append(review)
    return list


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

    dining_hall_empty_new_list = []
    for i in reviews:
        if get_place(i) == dining_hall:
            dining_hall_empty_new_list.append(get_rating(i))
        else:
            pass
    return sum(dining_hall_empty_new_list)/len(dining_hall_empty_new_list)


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

    first_hall = average_rating(first)
    second_hall = average_rating(second)
    if first_hall >= second_hall:
        return first
    else:
        return second
