## FAILED, Church encoding of pairs, so it is storing a values in a function and then you have to pass a function to the "pair" function data type to unravel it 


# Good morning! Here's your coding interview problem for today.

# This problem was asked by Jane Street.

# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. 
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

# Given this implementation of cons:

# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair
# Implement car and cdr.


import unittest

def car(pair):
    return pair(lambda x,y: x)

def cdr(pair):
    return pair(lambda x,y: y)

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


class Test_Problem(unittest.TestCase):
    def setUp(self):
        self.car = car
        self.cdr = cdr

    def test_correct(self):
        pair = cons(3,4)        
        self.assertEqual(self.car(pair), 3)
        self.assertEqual(self.cdr(pair), 4)

if __name__ == "__main__":
    pair = cons(3,4)
    
    print(car(pair), cdr(pair))

    unittest.main()