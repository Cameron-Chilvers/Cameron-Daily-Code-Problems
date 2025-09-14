## SUCCESS, sliding window and the slicing, I believe there is a way to make it using number tho
## FAILED, not in O(n) used deque to store the largest number in the set

# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

# 10 = max(10, 5, 2)
# 7 = max(5, 2, 7)
# 8 = max(2, 7, 8)
# 8 = max(7, 8, 7)
# Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.

import unittest

def problem(nums, k):
    if len(nums) < k:
        return []
    
    if len(nums) == k:
        max_ = max(nums)
        print(max_)
        return [max_]
            
    res = []
    deque = []
    start = 0
    for end, val in enumerate(nums):
        
        while len(deque) != 0 and nums[deque[-1]] < val:
            deque.pop()
        deque.append(end)

        if end-start+1 == k:
            max_ = nums[deque[0]]
            print(max_)
            res.append(max_)

            start += 1

            if deque[0] < start:
                deque.pop(0)

    return res

class Test_Problem(unittest.TestCase):
    def test_example(self):
        self.assertEqual(problem([10,5,2,7,8,7], 3), [10,7,8,8])
        self.assertEqual(problem([1,2,3,4,5,6], 2), [2,3,4,5,6])
        self.assertEqual(problem([1,2,3,4,5,6], 4), [4,5,6])
        self.assertEqual(problem([], 7), [])
        self.assertEqual(problem([1223,4526,826], 7), [])
        self.assertEqual(problem([1223,4526,826], 3), [4526])

if __name__ == "__main__":
    unittest.main()