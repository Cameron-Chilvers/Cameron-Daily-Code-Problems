## SUCCESS I USED THE SLIDING WINDOW METHOD CORRECTLY AND SOLVED THE QUESTION 

# Good morning! Here's your coding interview problem for today.

# This problem was asked by Amazon.

# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

import unittest

def problem(s, k):
    stor = dict()
    start, end = 0, 0
    max_sub_s = ''

    def add(char):
        nonlocal stor
        if char in stor:
            stor[char] += 1
        else:
            stor[char] = 1
    
    def remove(char):
        nonlocal stor
        stor[char] -= 1

        if stor[char] == 0:
            del stor[char]

    while end < len(s):
        add(s[end])
        end += 1

        while len(stor) > k:
            remove(s[start])
            start += 1

        max_sub_s = max_sub_s if len(max_sub_s) > end - start else s[start:end]

    return max_sub_s


class Test_Problem(unittest.TestCase):
    def test_example(self):
        self.assertEqual(problem("abcba", 2), "bcb")
        self.assertEqual(problem("abbbbcba", 2), "bbbbcb")
        self.assertEqual(problem("abbbbcba", 3), "abbbbcba")
        self.assertEqual(problem("abbbbcbaddd", 3), "abbbbcba")
        self.assertEqual(problem("abbbbcbaddd", 3), "abbbbcba")
        self.assertEqual(problem("aaaaaaaa", 3), "aaaaaaaa")

    def test_empty_string(self):
        self.assertEqual(problem("", 2), "")

    def test_k_zero(self):
        self.assertEqual(problem("abc", 0), "")

    def test_k_greater_than_unique_chars(self):
        self.assertEqual(problem("abc", 10), "abc")

    def test_single_char_string(self):
        self.assertEqual(problem("a", 1), "a")
        self.assertEqual(problem("a", 2), "a")

    def test_all_unique(self):
        self.assertEqual(problem("abcdef", 2), "ef")  # any 2-char substring valid
        self.assertEqual(problem("abcdef", 3), "def") # longest is 3 chars

    def test_long_repeated_pattern(self):
        self.assertEqual(problem("abababababab", 2), "abababababab")  # full string
        self.assertEqual(problem("abababababab", 1), "b")  # or "b", any 1-char

    def test_ties(self):
        # "abba" with k=2 could return "abba"
        self.assertEqual(problem("abba", 2), "abba")
        # "abcabc" with k=2 would give "bc"
        self.assertEqual(len(problem("abcabc", 2)), 2)

if __name__ == "__main__":
    unittest.main()