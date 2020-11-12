"""
DSC 20 HW 07
NAME:
PID:
"""

## Question 1.1 ##

def populate_menu_schedule(menu_schedule, recipe_dict):
    """
    Populate the given menu_schedule with recipes based on recipe_dict

    Parameters:
    menu_schedule (tuple): A tuple with five dictionaries representing the menu
    recipe_dict (dict): A dictionary of food recipe

    Returns:
    (None)

    >>> menu_schedule = ( \
            {"Orange Chicken": [], "Broccoli Beef": []}, \
            {"Broccoli Beef": []}, \
            {"Orange Chicken": [], "Spring Roll": []}, \
            {"Fortune Cookie": []}, \
            {"Fortune Cookie": [], "Broccoli Beef": []} \
        )
    >>> recipe_dict = { \
	        "Orange Chicken": ["Orange", "Chicken"], \
	        "Fortune Cookie": ["Fortune", "Cookie", "Paper"], \
	        "Spring Roll": ["Egg"] \
        }
    >>> populate_menu_schedule(menu_schedule, recipe_dict)
    >>> menu_schedule
    ({'Orange Chicken': ['Orange', 'Chicken']}, {}, {'Orange Chicken': \
['Orange', 'Chicken'], 'Spring Roll': ['Egg']}, {'Fortune Cookie': \
['Fortune', 'Cookie', 'Paper']}, {'Orange Chicken': ['Orange', 'Chicken']})
    >>> menu_schedule[0]['Orange Chicken'].append("Hot Sauce")
    >>> menu_schedule[2]['Orange Chicken']
    ['Orange', 'Chicken', 'Hot Sauce']
    >>> menu_schedule[0]['Gyro Plate'] = ['Beef']
    >>> menu_schedule[0]
    {'Orange Chicken': ['Orange', 'Chicken', 'Hot Sauce'], 'Gyro Plate': \
['Beef']}
    >>> menu_schedule[4]
    {'Orange Chicken': ['Orange', 'Chicken', 'Hot Sauce']}

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    """
    # magic numbers
    TUP_IDX_FOR_FRIDAY = 4

    # duplicate, or deep copy, recipe_dict
    recipe_dict_dup = {key:val[:] for key,val in recipe_dict.items()}

    for i in range( len(menu_schedule) ):
        menu = menu_schedule[i]
        # if is Friday's menu
        if i == TUP_IDX_FOR_FRIDAY:
            menu.clear()
            monday_menu = menu_schedule[0]
            menu.update(monday_menu)
            break

        dish_to_delete = []
        for dish in menu:
            if dish in recipe_dict_dup:
                menu[dish] = recipe_dict_dup[dish]
            else:
                dish_to_delete.append(dish)

        # delete the dishes that are absent in recipe_dict
        for to_delete in dish_to_delete:
            del menu[to_delete]


## Question 1.2 ##

def dereference_recipes(menu_schedule):
    """
    Dereference all pairs of recipe that refers to the same recipe object

    Parameters:
    menu_schedule (tuple): A tuple with five dictionaries representing the menu
        whose recipes have been already populated

    Returns:
    (None)

    >>> menu_schedule = ( \
            {"Orange Chicken": [], "Broccoli Beef": []}, \
            {}, \
            {}, \
            {}, \
            {"Orange Chicken": [], "Broccoli Beef": []} \
        )
    >>> oc_recipe = ['Orange', 'Chicken']
    >>> bb_recipe = ['Love']
    >>> menu_schedule[0]["Orange Chicken"] = oc_recipe
    >>> menu_schedule[4]["Orange Chicken"] = oc_recipe
    >>> menu_schedule[0]["Broccoli Beef"] = bb_recipe
    >>> menu_schedule[4]["Broccoli Beef"] = bb_recipe
    >>> menu_schedule[4]["Broccoli Beef"].append('Peace')
    >>> dereference_recipes(menu_schedule)
    >>> menu_schedule[4]["Broccoli Beef"].remove('Peace')
    >>> menu_schedule[0]["Broccoli Beef"]
    ['Love', 'Peace']

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    """

    DAYS_OF_A_WEEK = 5

    # shallow copy of menu_schedule
    menu_schedule_copy = menu_schedule
    # outer loop
    for i in range(DAYS_OF_A_WEEK):
        menu1 = menu_schedule[i]
        for dish1, recipe1 in menu1.items():

            # inner loop
            for j in range(i+1, DAYS_OF_A_WEEK):
                menu2 = menu_schedule_copy[j]
                for dish2, recipe2 in menu2.items():

                    # comparison logic
                    if recipe1 is recipe2:
                        menu2[dish2] = recipe1[:]

## Question 2 is in hw07_OOP.py ##

## Question 3.1 ##

def create_palindrome_v1(start, end):
    """
    Creates a palindrome of integers starting from start, ending at end
    (in the middle) All inputs are positive integers. No input validation
    required.
    Parameters: start, end (int), positive integers
    Returns: palindrome sequence (str)
    Restrictions. You should use recursion in this question.
    >>> create_palindrome_v1(1, 1)
    '1'
    >>> create_palindrome_v1(3, 5)
    '34543'
    >>> create_palindrome_v1(5, 2)
    '5432345'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    """
    inc_or_dec = (start < end) * 2 - 1

    if start == end:
        return '{0}'.format(end)
    else:
        return '{0}'.format(start)\
        + create_palindrome_v1(start\
        + inc_or_dec, end) + '{0}'.format(start)

## Question 3.2 ##

def create_palindrome_v2(start1, end1, start2, end2):
    """
    Creates a two level palindrome of integers. The first level (outer level)
    starts from start1 and ends at end1. The second level (inner level) starts
    from start2 and end2. No input validation is required.
    Parameters: start1, end1, start2, end2 (int), positive integers
    Returns: palindrome sequence (str)
    Restrictions. You should use recursion in this question.
    >>> create_palindrome_v2(1, 1, 1, 1)
    '1_1_1'
    >>> create_palindrome_v2(2, 5, 5, 4)
    '2345_545_5432'
    >>> create_palindrome_v2(3, 1, 5, 9)
    '321_567898765_123'
    
    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    """
    inc_or_dec = (start1 < end1) * 2 - 1

    if start1 == end1:
        first_pali = create_palindrome_v1(start2, end2)
        return '{0}_'.format(start1) + first_pali + '_{0}'.format(start1)
    else:
        return '{0}'.format(start1) +\
        create_palindrome_v2(start1 + inc_or_dec, end1, start2, end2)\
        + '{0}'.format(start1)
