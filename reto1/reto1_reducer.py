#!/usr/bin/env python
"""reto1_reducer.py"""

from operator import itemgetter
import sys
#Reducer para el Reto 1 del Laboratorio 1 de Big Data

class Stack:
    """Simple Stack (No hay garantia que se tenga numpy)"""

    #Values of the stack
    values = []
    #Names of the corresponding values
    names = []
    #Minimum integer aloud
    min_value = -sys.maxint - 1

    def insert(self, name, value):
        if(value > self.min_value):
            inserted = False
            for i in range(len(self.values) - 1):
                #checks for insertion place
                if(value >= self.values[i] and value < self.values[i + 1]):

                    #inserts
                    self.values = self.values[0:(i+1)] + [value] + self.values[(i+1):]
                    self.names = self.names[0:(i+1)] + [name] + self.names[(i+1):]

                    #inserted
                    inserted = True
                    break

            if not inserted:
                #Adds the element at the end of stack
                self.values.append(value)
                self.names.append(name)

            #Keeps maximum size
            #Checks if there are any extra elements
            # and grabs the tail
            dif = len(self.names) - min(len(self.names),self.max_size)
            self.values = self.values[dif:]
            self.names = self.names[dif:]

            if(len(self.values) == self.max_size):
                self.min_value = self.values[0]

    def export(self):
        for i in range(len(self.values)):
            print '%s\t%s' % (self.names[i], self.values[i])


    def __init__(self, max_size):
        if(max_size <= 0):
            raise ValueError('Stack maximum should be greater tha zero. Received: ' + str(max_size))

        self.max_size = max_size

#end of stack class

max_titles = 10
stack = Stack(max_titles)

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    title, length = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        length = int(length)
    except ValueError:
        # length was not a number
        raise ValueError('Length was not a number: ' + str(length))

    # Inserts the title and length to stack
    stack.insert(title, length)

#Exports top Stack
stack.export()
