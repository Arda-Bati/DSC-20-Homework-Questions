import numpy as np


class Stack():
   
    def __init__(self, size):

        self.items = np.empty(size, dtype = str)
        self.nelem = 0
        self.top = 0

    def push(self, elem):

        if (self.top != len(self.items)):
            self.items[self.top] = elem
            self.nelem = self.nelem + 1
            self.top +=1
        else:
            print("No space to add elements")

    def pop(self):
        if self.nelem == 0:
            print("No elements to remove")
        else:
            value = self.items[self.top-1]
            self.nelem = self.nelem - 1
            self.top = self.top - 1
            return value

    def peek(self):
        if self.nelem == 0:
            print("No elements to remove")
        else:
            return self.items[self.top-1]

    def isEmpty(self):
        if self.nelem == 0:
            return True
        else:
            return False

    def size(self):
        return self.nelem

    def __str__(self):

        if self.nelem == 0:
            return '(bottom)(top)'

        output = '(bottom)'
        for i in range(self.nelem - 1):
            output = output + str(self.items[i])+" -> "

        output = output + str(self.items[self.nelem - 1])+'(top)'
        return output

        