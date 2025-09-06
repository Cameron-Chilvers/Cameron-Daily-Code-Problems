## Failed, New it was dp but could not find the correct exit cases for the solution


# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

# Given the root to a binary tree, count the number of unival subtrees.

# For example, the following tree has 5 unival subtrees:

#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1

import unittest
from typing import Optional


# Test scaffolding (used only to build trees in tests)
class TreeNode:
    def __init__(self, val: int, left: Optional["TreeNode"]=None, right: Optional["TreeNode"]=None):
        self.val = val
        self.left = left
        self.right = right

def N(v, l=None, r=None):
    return TreeNode(v, l, r)


def count_unival_subtrees(n: TreeNode)->int:
    def ways(n:TreeNode):
        if n is None:
            return True, 0   # empty tree is unival, count=0

        left_is_unival, left_count = ways(n.left)
        right_is_unival, right_count = ways(n.right)

        total = left_count + right_count

        # Check if current node is unival
        if left_is_unival and right_is_unival:
            if (n.left and n.left.val != n.val) or (n.right and n.right.val != n.val):
                return False, total
            
            # current subtree is unival
            return True, total + 1

        return False, total


    return ways(n)[1]

class Test_Problem(unittest.TestCase):
    def test_empty_tree(self):
        self.assertEqual(count_unival_subtrees(None), 0)

    def test_single_node(self):
        root = N(1)
        self.assertEqual(count_unival_subtrees(root), 1)

    def test_two_nodes_same_value(self):
        root = N(1, N(1), None)
        self.assertEqual(count_unival_subtrees(root), 2)

    def test_two_nodes_different_value(self):
        root = N(1, N(2), None)
        self.assertEqual(count_unival_subtrees(root), 1)

    def test_all_same_values_full_tree(self):
        #      1
        #     / \
        #    1   1
        #   / \ / \
        #  1  1 1  1
        root = N(1,
                 N(1, N(1), N(1)),
                 N(1, N(1), N(1)))
        # Every node forms a unival subtree => 7
        self.assertEqual(count_unival_subtrees(root), 7)

    def test_mixed_values(self):
        # Example from prompt (expected 5):
        #    0
        #   / \
        #  1   0
        #     / \
        #    1   0
        #   / \
        #  1   1
        root = N(0,
                 N(1),
                 N(0,
                   N(1, N(1), N(1)),
                   N(0)))
        self.assertEqual(count_unival_subtrees(root), 5)

    def test_left_skew(self):
        # 1
        #  \
        #   1
        #    \
        #     1
        root = N(1, None, N(1, None, N(1)))
        self.assertEqual(count_unival_subtrees(root), 3)

    def test_right_skew_with_break(self):
        # 1
        #  \
        #   1
        #    \
        #     2
        root = N(1, None, N(1, None, N(2)))
        # Leaves (2 and 1) are unival; the middle node (1->2) not; root not
        self.assertEqual(count_unival_subtrees(root), 1)

    def test_subtree_unival_but_parent_not(self):
        #     2
        #    / \
        #   2   2
        #      /
        #     3
        root = N(2, N(2), N(2, N(3), None))
        # Leaves: left 2, leaf 3, right 2 (with left child 3) is not unival,
        # left child 2 is unival, each leaf is unival. Total = 2
        self.assertEqual(count_unival_subtrees(root), 2)

    def test_example(self):
        #    0
        #   / \
        #  1   0
        #     / \
        #    1   0
        #   / \
        #  1   1
        root = N(0, N(1), N(0, N(0), N(1, N(1), N(1))))
        # Leaves: left 2, leaf 3, right 2 (with left child 3) is not unival,
        # left child 2 is unival, each leaf is unival. Total = 2
        self.assertEqual(count_unival_subtrees(root), 5)

    def test_duplicate_values_with_mixed_children(self):
        #     5
        #    / \
        #   5   5
        #  / \   \
        # 5   4   5
        root = N(5,
                 N(5, N(5), N(4)),
                 N(5, None, N(5)))
        # Unival: all leaf 5's (3), leaf 4 (1), right subtree (5->5) (1), left subtree not, root not
        self.assertEqual(count_unival_subtrees(root), 4)

if __name__ == "__main__":

    unittest.main()