## SUCCESS, did not get most optimal solution missed memo knew what is was and I could implement


# Good morning! Here's your coding interview problem for today.

# This problem was asked by Amazon.

# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. 
# Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

# For example, if N is 4, then there are 5 unique ways:

# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2

# What if, instead of being able to climb 1 or 2 steps at a time, 
# you could climb any number from a set of positive integers X? 
# For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

import unittest

def problem(n, steps):
    if n <= 0: # if num not possible
        return 0

    def climb_steps(num, steps, memo):
        if num < 0: # over so dont count
            return 0
        
        if num == 0: # correct so return one
            return 1
        
        if num in memo: # checking the memo
            return memo[num]
        
        # recursive
        total = 0
        for step in steps:
            total += climb_steps(num - step, steps, memo)
        
        memo[num] = total
        return total # recursive down all the steps

    return climb_steps(n, steps, {})

class Test_Problem(unittest.TestCase):
    def test_example(self):
        self.assertEqual(problem(5, {1,3,5}), 5)
        self.assertEqual(problem(4, {1,2}), 5)
        self.assertEqual(problem(0, {1,2}), 0)
        self.assertEqual(problem(1, {3,2}), 0)
        self.assertEqual(problem(-1, {3,2}), 0)
        self.assertEqual(problem(962, {961,2}), 1)
        self.assertEqual(problem(5, {1,2,3}), 13)
    
if __name__ == "__main__":
    unittest.main()
