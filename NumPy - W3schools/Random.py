

########################################################
#          Page 1: Random Numbers in NumPy
########################################################


from numpy import random

x = random.randint(100)
print(x)
#49






x = random.rand()
print(x)
#0.6548585035580182









"""
Integers
The randint() method takes a size 
    parameter where you can specify the shape of an array.
"""

x=random.randint(100, size=(5))
print(x)
#[96 44  4 90 56]


x = random.randint(100, size=(3, 5))
print(x)
"""
[[94 83 34 19 14]
 [83 43 90  9 36]
 [71 52  7 68 76]]
"""











"""
Floats
The rand() method also allows you to specify the shape of the array.
"""


x = random.rand(5)
print(x)
#[0.27565646 0.36023494 0.49352355 0.89172373 0.71604923]





x = random.rand(3, 5)
print(x)
"""
[[0.46870078 0.5743895  0.63754437 0.22653259 0.32546415]
 [0.99252935 0.10930629 0.11466714 0.90390978 0.52149155]
 [0.84595462 0.09078936 0.82627313 0.45569995 0.75975826]]
"""













"""
Generate Random Number From Array
The choice() method allows you to generate a 
    random value based on an array of values.

The choice() method takes an array as a 
    parameter and randomly returns one of the values.
"""

x = random.choice([3, 5, 7, 9])

print(x)
#7








########################################################
#          Page 2: Random Data Distribution
########################################################

"""
Random Distribution
A random distribution is a set of random 
    numbers that follow a certain probability density function.

Probability Density Function: A function 
    that describes a continuous probability. 
    i.e. probability of all values in an array.
"""


"""

Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9.

The probability for the value to be 3 is set to be 0.1

The probability for the value to be 5 is set to be 0.3

The probability for the value to be 7 is set to be 0.6

The probability for the value to be 9 is set to be 0
"""

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))

print(x)
"""
[5 7 5 7 7 5 5 7 5 7 3 7 7 7 7 5 5 7 7 7 7 7 3 7 7 7 7 7 3 7 7 3 5 7 7 5 7
 5 7 7 7 7 7 7 5 7 7 7 7 7 7 7 3 5 5 7 7 7 5 7 5 5 5 3 7 5 5 7 7 5 5 7 5 7
 5 7 7 5 7 5 7 7 7 3 7 7 3 5 7 5 7 7 3 7 7 5 3 7 7 7]
"""








