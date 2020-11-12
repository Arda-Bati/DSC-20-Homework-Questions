from stack import Stack
import numpy as np

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

    st = Stack(len(expression))
    split = list(expression)

    for i in range(len(expression)):

        if split[i]=='(' or split[i]=='{' or split[i]=='[':
            st.push(split[i])

        elif (split[i]==')'):
            if st.isEmpty():
                return False
            else:
                elem = st.pop()
                if elem != '(':
                    return False

        elif (split[i]==']'):
            if st.isEmpty():
                return False
            else:
                elem = st.pop()
                if elem != '[':
                    return False

        elif (split[i]=='}'):
            if st.isEmpty():
                return False
            else:
                elem = st.pop()
                if elem != '{':
                    return False

        else: continue

    if st.size() > 0:
        return False
    else:
        return True


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
        self.front = 0
        self.rear = 0
        self.num_elems = 0
        self.capacity=capacity
        self.data=np.array([None for _ in range(self.capacity)])
        self.expand_factor = 2

    def dequeue(self):
        """
        dequeues from the front of the queue

        >>> q = Queue()
        >>> q.dequeue()
        Attempt to dequeue from an empty queue
        """
        #Your Code Here
        try:
            if self.is_empty():
                raise IndexError('Attempt to dequeue from an empty queue')
        except IndexError as e:
            print(str(e))
        else:
            #update number of elements in the queue and front element index
            self.num_elems -= 1
            self.front += 1

            #check special case: front has reaches the largest index
            if self.front == self.capacity:
                self.front = 0
                return self.data[-1]
            else: #normal case
                return self.data[self.front-1]



    def enqueue(self,elem):
        """
        enqueue at the rear of the queue
        >>> q = Queue()
        >>> q.enqueue("a")
        """
        #Your Code Here
        #update number of elements in the queue and rear element index
        self.num_elems += 1
        self.rear += 1

        #special case: rear reaches the largest index
        if self.rear == self.capacity and (not self.is_full()):
            self.rear=0
            self.data[-1]=elem

        #special case: reaches maximum capacity
        elif self.is_full():
            self.expand()
            self.data[self.rear-1]=elem

        #normal case
        else:
            self.data[self.rear-1]=elem

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
        #double the capacity
        self.capacity *= self.expand_factor

        #initialize a termporary list for transferring data
        temp = np.array([None for _ in range(self.capacity)])

        #transfer data to new list
        for i in range(self.num_elems):
            temp[i]=self.dequeue()

        #update self.data
        self.data=temp

        #udpate indices and element count
        self.front=0
        self.num_elems=self.capacity//2
        self.rear=self.num_elems


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
        return self.num_elems == self.capacity


    def is_empty(self):
        """
        checks if circular array is empty
        >>> q = Queue()
        >>> q.is_empty()
        True
        """
        #Your Code Here
        return self.num_elems == 0

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
        if self.is_empty():
            print('[]')
        elif self.front<self.rear:
            print('[ | {0} | ]'.format(' | '.join(\
                [str(self.data[i]) for i in range(self.front,self.rear)])))
        else:
            f = ' | '.join([str(self.data[i]) for i in range(self.front,self.capacity)])
            r = ' | '.join([str(self.data[i]) for i in range(self.rear)])

            print('[ | {0} | {1} | ]'.format(f,r))

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
    try:
        if not isinstance(m,int) or isinstance(n,int):
            raise TypeError("Invalid input data type.")
        elif m<=0 or n<=0:
            raise ValueError("m and n should be positive!")
    except (TypeError, ValueError) as e:
        print(str(e))

    else:
        queue = Queue()
        for i in range(n):
            queue.enqueue(i+1)
        while(queue.num_elems > 1):
            for _ in range(m-1):
                last = queue.dequeue()
                queue.enqueue(last)
            print(queue.dequeue())
        return queue.dequeue()
