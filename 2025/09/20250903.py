## Failed, was not able to break down the problem as in DP, 


# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

# You can assume that the messages are decodable. For example, '001' is not allowed.


import unittest

mapping = {i-96: chr(i) for i in range(97, 97+26)}

def problem(message: str)->int:
    memo = {}

    def ways(i: int)->int:
        if i in memo:
            return memo[i]
        if i == len(message):
            return 1
        if message[i] == '0':
            return 0
        
        total = ways(i+1) # go up one digit

        if i+1 < len(message) and (message[i] =='1' or (message[i] == '2' and message[i+1] <= '6')):
            total += ways(i+2)

        memo[i] = total
        return total

    return ways(0)


class Test_Problem(unittest.TestCase):
    def test_basic_examples(self):
        self.assertEqual(problem("111"), 3)   # "aaa", "ka", "ak"
        self.assertEqual(problem("113"), 3)   # "aac","kc","am"
        self.assertEqual(problem("12"), 2)    # "ab","l"
        self.assertEqual(problem("123"), 3)   # "abc","aw","lc"
        self.assertEqual(problem("226"), 3)   # "bbf","bz","vf"

    def test_single_and_empty(self):
        self.assertEqual(problem(""), 1)      # by convention: one way to decode empty
        self.assertEqual(problem("1"), 1)
        self.assertEqual(problem("9"), 1)

    def test_with_zeros_valid(self):
        self.assertEqual(problem("10"), 1)    # "j"
        self.assertEqual(problem("20"), 1)    # "t"
        self.assertEqual(problem("101"), 1)   # "10" + "1"
        self.assertEqual(problem("2101"), 1)  # "2" + "101"

    # def test_with_zeros_invalid(self):
    #     # If you truly assume inputs are decodable, you can skip these, but they're useful to expose bugs.
    #     self.assertEqual(problem("0"), 0)
    #     self.assertEqual(problem("30"), 0)
    #     self.assertEqual(problem("100"), 0)
    #     self.assertEqual(problem("01"), 0)

    def test_bounds_two_digit_over_26(self):
        self.assertEqual(problem("27"), 1)    # "2","7" only
        self.assertEqual(problem("28"), 1)
        self.assertEqual(problem("29"), 1)

    def test_mixed_complex(self):
        self.assertEqual(problem("11106"), 2) # "1 1 10 6", "11 10 6"

    def test_long_all_ones(self):
        # For a run of '1's without zeros, count follows Fib(n+1)
        # n=6 -> 13
        self.assertEqual(problem("111111"), 13)


if __name__ == "__main__":
    # Create the first node (head of the list)
    print(mapping)
    print("1"[2:])
    print(problem("101"))
    # print(problem('111'))
    # print(problem('113'))

    unittest.main()