## PASSED


# Good morning! Here's your coding interview problem for today.

# This problem was recently asked by Google.

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?

import unittest

def problem(nums, k):
    stor = dict()

    for i, num in enumerate(nums):
        remain = k - num
        if num in stor:
            return True
        else:
            stor[remain] = i
            
    return False


class Test_Problem(unittest.TestCase):
    def test_correct(self):
        nums = [1,2,3] 
        k = 5
        self.assertEqual(problem(nums, k), True)

    def test_example(self):
        nums = [10, 15, 3, 7]
        k = 17
        self.assertEqual(problem(nums, k), True)

    def test_false(self):
        nums = [1,2,2,2] 
        k = 5
        self.assertEqual(problem(nums, k), False)

    def test_double_same(self):
        nums = [1,3,3] 
        k = 6
        self.assertEqual(problem(nums, k), True)

    def test_negative_true(self):
        nums = [-2,3,3,8] 
        k = 6
        self.assertEqual(problem(nums, k), True)

    def test_negative_false(self):
        nums = [-2,6,3,9] 
        k = 6
        self.assertEqual(problem(nums, k), False)

if __name__ == '__main__':
    # nums = [10, 15, 3, 7]
    # k = 17
    # print(problem(nums, k))

    unittest.main()
