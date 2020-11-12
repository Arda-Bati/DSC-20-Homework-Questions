
# Question 1.1:


def question1_1():
    """Return a list with answers to the True/False question
    >>> out = question1_1()
    >>> type(out) == list
    True
    >>> len(out)
    10
    >>> all([isinstance(i, bool) for i in out])
    True
    """

# Question 2.2:

def question1_2():
    """Return a list with answer about code complexity
    >>> out = question1_2()
    >>> type(out) == list
    True
    >>> len(out)
    10
    >>> all([isinstance(i, int) and i<=7 and i>=1 for i in out])
    True
    """

# Question 2.1:

def make_id(name, suffix):
    """Returns a netid for name with suffix n.
    >>> make_id('Marina Aleksandrovna Langlois', 17)
    'mal17'
    >>>
    """    


# Question 2.2:

def do_you_have_me(dic, item):
    """Returns a key for which item exists
    otherwise returns "Not there"
    >>> do_you_have_me({"key1":[1,2,3,4], "key2": [5,4,7,8]}, 9)
    'Not there'
    >>> do_you_have_me({"key1":[1,2,3,4], "key2": [5,4,7,8]}, 1)
    'key1'
    >>> do_you_have_me({"key1":[1,2,3,4], "key2": [5,4,7,8]}, 4)
    'key1'
    """

# Question 2.3:

def read_menus(food_cat, *menus):
    """Return a string that summarized amount of items from the same category
    in the menus.
    >>> read_menus("food_cat.txt", "menu1.txt", "menu2.txt")
    'There are 7 burgers, 4 salads and 5 desserts'
    """
    









