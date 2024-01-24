from qiskit import *
from qiskit.visualization import plot_histogram
import time
from matplotlib import pyplot as plt
import sys

# Classical search algorithm O(n)

mylist = [ 7, 4, 1, 5, 0, 8, 2, 3, 9 ]

# Oracle (black box) - unknown function that does something unknown
def oracle(number):
    return number == 8

for index, number in enumerate(mylist):
    if oracle(number):
        print('Found winning number {} at index {} execution count {}'.format(number, index, index+1))
        break

