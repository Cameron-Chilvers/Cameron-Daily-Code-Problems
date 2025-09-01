## PASSED


# Good morning! Here's your coding interview problem for today.

# This problem was asked by Uber.

# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

import unittest

def problem(nums):
    if len(nums) == 0:
        return []
    elif len(nums) == 1:
        return [0]
    elif len(nums) == 2:
        return nums[::-1]    

    total = 1
    for num in nums:
        total *= num

    res = list()
    for num in nums:
        res.append(total / num)

    return res

def problem_no_divide(nums):
    if len(nums) == 0:
        return []
    elif len(nums) == 1:
        return [0]
    elif len(nums) == 2:
        return nums[::-1]

    forward_res = list()
    backward_res = list()

    # Populating forward
    for num in nums:
        if len(forward_res) == 0:
            forward_res.append(num)
        else:
            forward_res.append(num * forward_res[-1])

    for num in nums[::-1]:
        if len(backward_res) == 0:
            backward_res.append(num)
        else:
            backward_res.append(num * backward_res[-1])
    backward_res = backward_res[::-1]
    
    res = list()
    for i in range(len(nums)):
        if i == 0:
            res.append(backward_res[1])
        elif i == len(nums)-1:
            res.append(forward_res[-2])
        else:
            res.append(forward_res[i-1] * backward_res[i+1])

    return res

class Test_Problem(unittest.TestCase):
    def test_correct(self):
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(problem_no_divide(nums), [120, 60, 40, 30, 24])

    def test_2(self):
        nums = [3, 2, 1]
        self.assertEqual(problem_no_divide(nums), [2, 3, 6])

    def test_no_values(self):
        nums = []
        self.assertEqual(problem_no_divide(nums), [])
    
    def test_one_value(self):
        nums = [1]
        self.assertEqual(problem_no_divide(nums), [0])

    def test_two_values(self):
        nums = [9,4]
        self.assertEqual(problem_no_divide(nums), [4,9])

    def test_negative(self):
        nums = [-1,3,-6,6,-4]
        self.assertEqual(problem_no_divide(nums), [432, -144, 72, -72, 108])

if __name__ == '__main__':
    nums = [-1,3,-6,6,-4]
    print(problem_no_divide(nums))

    unittest.main()
