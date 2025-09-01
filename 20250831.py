## FAILED, use Cyclic Sort-style algorithm, where you sort in place by swapping by value and index


# Good morning! Here's your coding interview problem for today.

# This problem was asked by Stripe.

# Given an array of integers, find the first missing positive integer in linear time and constant space. 
# In other words, find the lowest positive integer that does not exist in the array. 
# The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.

import unittest

def problem(nums) -> int:
    if len(nums) == 0:
        return 1
    
    # Change negative to zero to find lowest one
    new = []
    for num in nums:
        if num >= 0:
            new.append(num)
        else:
            new.append(0)

    sort_nums = sorted(new)
    
    for i in range(len(sort_nums)-1):
        if sort_nums[i]+1 != sort_nums[i+1] and sort_nums[i] != sort_nums[i+1]: # filter duplicates
            return sort_nums[i]+1 # Find where the missing number is

    return sort_nums[-1]+1

def problem_2(nums):
    n = len(nums)
    i = 0
    while i < n:
        # correct index for nums[i]
        correct = nums[i] - 1
        # only swap if nums[i] is in range and not already in correct position
        if 1 <= nums[i] <= n and nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1
    
    # find the first index where nums[i] != i+1
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1
        

class Test_Problem(unittest.TestCase):
    def setUp(self):
        self.func = problem_2

    def test_correct(self):
        nums = [3, 4, -1, 1]
        self.assertEqual(self.func(nums), 2)

        nums = [1, 2, 0]
        self.assertEqual(self.func(nums), 3)

        nums = [0]
        self.assertEqual(self.func(nums), 1)

        nums = []
        self.assertEqual(self.func(nums), 1)

        nums = [1, 2, 1, 2, 4]
        self.assertEqual(self.func(nums), 3)

        nums = [-1, -2, -1, -2, 4]
        self.assertEqual(self.func(nums), 1)

        nums = [-5, -3, -1]
        self.assertEqual(self.func(nums), 1)

        nums = [1, 2, 3, 4, 5] 
        self.assertEqual(self.func(nums), 6)

        nums = [7, 8, 9, 11, 12]
        self.assertEqual(self.func(nums), 1)

        nums = [2]
        self.assertEqual(self.func(nums), 1)

        nums = [1]
        self.assertEqual(self.func(nums), 2)


if __name__ == "__main__":
    nums = [1,1,2,2,3,4,4]

    print(problem_2(nums))

    # unittest.main()