# Question 1.1
def question1_1():
    '''
    >>> out = question1_1()
    >>> type(out) == list
    True
    >>> len(out)
    10
    >>> all([isinstance(i, bool) for i in out])
    True
    '''
    return [True, True, True, False, False, False, True, False, True, True]

# Question 1.2
def question1_2():
    '''
    >>> out = question1_2()
    >>> type(out) == list
    True
    >>> len(out)
    10
    >>> all([isinstance(i, int) and i<=7 and i>=1 for i in out])
    True
    '''
    return [1, 2, 3, 4, 5, 7, 1, 3, 4, 5]

# Question 2.1
def make_id(name, suffix):
    '''
    Returns a netid for name with suffix n.
    >>> make_id('Marina Aleksandrovna Langlois', 17)
    'mal17'
    >>>
    '''
    name = name.lower()     # switch to lower case
    fpos = name.find(' ')   # find first space
    first = name[:fpos]
    last = name[fpos+1:]
    mpos = last.find(' ')    # see if there is another space
    if mpos == -1:
        return first[0]+last[0]+str(suffix)  # remember, n is not a string
    else:
        middle = last[:mpos]
        last = last[mpos+1:]
        return first[0]+middle[0]+last[0]+str(suffix)


# Question 2.2:
def do_you_have_me(dic, item):
    '''
    Returns a key for which item exists
    otherwise returns "Not there"
    >>> do_you_have_me({"key1":[1,2,3,4], "key2": [5,4,7,8]}, 9)
    'Not there'
    >>> do_you_have_me({"key1":[1,2,3,4], "key2": [5,4,7,8]}, 1)
    'key1'
    >>> do_you_have_me({"key1":[1,2,3,4], "key2": [5,4,7,8]}, 4)
    'key1'
    '''
    for key, value in dic.items():
        if item in value:
            return key
    return "Not there"


#print(do_you_have_me({"key1":[1,2,3,4], "key2": [5,4,7,8]}, 9))

# Question 2.3:

# helper 1 for Question 2.3
def from_list_to_dict(lst):
    '''
    Helper for read_menus
    '''
    dict_cat = {}
    for i in lst:
        value, key = i.split(":")
        key = key.strip()
        if key not in dict_cat:
            dict_cat[key] = [value]
        else:
            dict_cat[key].append(value)

    return(dict_cat)

# helper 2 for Question 2.3 
def food_counter(all_menues, dict_cat):
    '''
    Helper for read_menus
    '''
    num_burgers, num_salads, num_desserts = 0, 0, 0
    for i in all_menues:
        if i != '\n':
            name, calories = i.split(":")

            is_there = do_you_have_me(dict_cat, name)
            if is_there == "Burger":
                num_burgers += 1
            if is_there == "Salad":
                num_salads += 1
            if is_there == "Dessert":
                num_desserts += 1
    return num_burgers, num_salads, num_desserts


def read_menus(food_cat, *menus):
    '''Return a string that summirzed amount of items from the same category
    in the menus.
    >>> read_menus("food_cat.txt", "menu1.txt", "menu2.txt")
    'There are 7 burgers, 4 salads and 5 desserts'
    '''
    temp = []
    with open(food_cat, 'r') as f:
        temp = f.readlines()

    dict_cat = from_list_to_dict(temp)

    all_menues = []
    temp = []
    for m in menus:
        with open(m, 'r') as f:
            temp = f.readlines()
        all_menues = all_menues + temp
        temp = []

    num_burgers, num_salads, num_desserts = food_counter(all_menues, dict_cat)
    out = str.format("There are {} burgers, {} salads and {} desserts", \
        num_burgers, num_salads, num_desserts)
    return out
