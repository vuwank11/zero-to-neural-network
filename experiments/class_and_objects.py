"""
Created by:
    Author: Bhuwan Khatiwada
    Date: 25/12/2023
"""
import numpy as np

class Class:
    def __init__(self):
        self.value = np.random.randint(low=0, high=100)


if __name__ == '__main__':
    for i in range(10):

        _object = Class()

        print(Class.__instancecheck__(_object))

    isinstance()
    Class.__sizeof__()

