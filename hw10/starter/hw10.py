import numpy as np
from stack import Stack

def paren_checker(expression):
    """ Checks whether the pairs and the orders of 
    '{', '}', '(','), '[', ']' are correct in a
    given expression

    >>> paren_checker("(((]})")
    False
    >>> paren_checker("(")
    False
    >>> paren_checker("(){}[]")
    True
    >>> paren_checker("(   x   )")
    True
    >>> paren_checker("a()b{}c[]d")
    True
    >>> paren_checker("")
    True
    """
    #Your Code Here



class Queue:
    """
    A queue, dequeues from front and enqueues at rear
    >>> a=Queue()
    >>> a.enqueue(1)
    >>> a.enqueue(2)
    >>> a.enqueue(3)
    >>> a.enqueue(4)
    >>> a.enqueue(5)
    >>> a.print_queue()
    [ | 1 | 2 | 3 | 4 | 5 | ]
    >>> a.front
    0
    >>> a.rear
    5
    >>> a.data
    array([1, 2, 3, 4, 5, None, None, None, None, None], dtype=object)
    >>> a.capacity
    10
    >>> a.dequeue()
    1
    >>> a.print_queue()
    [ | 2 | 3 | 4 | 5 | ]
    >>> a.front
    1
    >>> a.rear
    5
    
    >>> a=Queue(10)
    >>> a.capacity
    10
    
    >>> b=Queue()
    >>> b.dequeue()
    Attempt to dequeue from an empty queue
    >>> b.enqueue(1)
    >>> b.enqueue(max)
    >>> b.print_queue()
    [ | 1 | <built-in function max> | ]
    >>> b.dequeue()
    1
    >>> b.dequeue()
    <built-in function max>
    >>> b.front
    2
    >>> b.rear
    2
    >>> b.dequeue()
    Attempt to dequeue from an empty queue
    """
    
    def __init__(self,capacity=5):
        """
        >>> q = Queue()
        """
        #Your Code Here
        
    
    def dequeue(self):
        """
        dequeues from the front of the queue
        
        >>> q = Queue()
        >>> q.dequeue()
        Attempt to dequeue from an empty queue
        """
        #Your Code Here
        
        
        

    def enqueue(self,elem):
        """
        enqueue at the rear of the queue
        >>> q = Queue()
        >>> q.enqueue("a")
        """
        #Your Code Here
        

    def expand(self):
        """
        expand the capacity of the circular array when needed
        >>> q = Queue()
        >>> q.capacity
        5
        >>> q.expand()
        >>> q.capacity
        10
        """
        #Your Code Here
        

    def is_full(self):
        """
        checks if circular array is full
        >>> q = Queue()
        >>> for i in range(4): q.enqueue(i)
        >>> q.data
        array([0, 1, 2, 3, None], dtype=object)
        >>> q.is_full()
        False
        """
        #Your Code Here
        
        

    def is_empty(self):
        """
        checks if circular array is full
        >>> q = Queue()
        >>> q.is_empty()
        True
        """
        #Your Code Here
        

    def print_queue(self):
        """
        prints out queue in a human-friendly format
        >>> q = Queue()
        >>> for i in range(5): q.enqueue(i)
        >>> q.print_queue()
        [ | 0 | 1 | 2 | 3 | 4 | ]
        >>> p = Queue()
        >>> p.print_queue()
        []
        """
        #Your Code Here
        


def cursed_carousel(n, m):
    """
    m is the number of customers in line
    n is the number of customers sent to the back of the line
    return the number of the customer which is last to be served
    
    >>> cursed_carousel(6,3)
    3
    6
    4
    2
    5
    1
    >>> cursed_carousel(-1,-2)
    m and n should be positive!
    >>> cursed_carousel('5','1')
    Invalid input data type.

    """
    #Your Code Here
    