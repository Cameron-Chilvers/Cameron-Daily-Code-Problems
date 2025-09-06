## PASSED, is house robber problem, remember how to break down the problem and go from there


# Good morning! Here's your coding interview problem for today.

# This problem was asked by Airbnb.

# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

# Follow-up: Can you do this in O(N) time and constant space?

import unittest

def problem(nums):
    if len(nums) == 0:
        return 0
    
    if len(nums) <= 2:
        return max(nums)
        
    prev_2 = nums[0]
    prev = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        cur_total = max(nums[i] + prev_2, prev)
        prev_2, prev = prev, cur_total

    return max(prev, prev_2)


class Test_Problem(unittest.TestCase):
    def test_example(self):
        self.assertEqual(problem([2, 4, 6, 2, 5]), 13)

    def test_example_2(self):
        self.assertEqual(problem([5, 1, 1, 5]), 10)

    def test_single_element(self):
        self.assertEqual(problem([7]), 7)

    def test_two_elements(self):
        self.assertEqual(problem([2, 10]), 10)
        self.assertEqual(problem([10, 2]), 10)

    def test_all_negatives(self):
        self.assertEqual(problem([-2, -4, -6, -8]), -2)

    def test_with_zeros(self):
        self.assertEqual(problem([0, 5, 0, 10]), 15)

    def test_large_gap(self):
        self.assertEqual(problem([100, 1, 1, 100]), 200)

    def test_adjacent_large_numbers(self):
        self.assertEqual(problem([10, 20, 30, 40]), 60)

    def test_alternating_pattern(self):
        self.assertEqual(problem([5, 1, 5, 1, 5]), 15)

    def test_longer_sequence(self):
        self.assertEqual(problem([3, 2, 7, 10]), 13)
        self.assertEqual(problem([3, 2, 5, 10, 7]), 15)

if __name__ == "__main__":

    unittest.main()