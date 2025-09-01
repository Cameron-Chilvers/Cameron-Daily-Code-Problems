## PASSED, use xml or better descriptors


# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

# For example, given the following Node class

# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The following test should pass:

# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'


import unittest

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(node: Node):
    # generate left
    if node.left == None and node.right == None:
        return "{'"+node.val+"':[{},{}]}"
    elif node.right == None:
        return "{'"+node.val+"':[" + serialize(node.left) + ",{}]}"
    elif node.left == None:
        return "{'"+node.val+"':[{}," + serialize(node.right) + "]}"

    # combine both
    return "{'" + node.val + "':[" + serialize(node.left) + "," + serialize(node.right) + "]}"

# very much valid parenteses
def find_middle(s: str):
    stack = []

    for i, c in enumerate(s):
        if c == "{":
            stack.append('{')
        elif c == "}":
            if stack[-1] != '{':
                raise Exception("Malformed string")

            stack.pop()

        if len(stack) == 0:
            return i +1

def deserialize(s: str):
    if len(s) <= 3:
        return None

    content = s[s.find('{') + 1 : s.rfind('}')]
    val = content[:content.find(":")].replace("'", "")
    nodes = content[content.find('[') + 1 : content.rfind(']')]


    left_str = nodes[:find_middle(nodes)]
    right_str = nodes[find_middle(nodes)+1:]

    return Node(val=val, left=deserialize(left_str), right=deserialize(right_str))

class TestProblem(unittest.TestCase):
    def test_serialize(self):
        node = Node('root', Node('left', Node('left.left')), Node('right'))
        
        self.assertEqual(serialize(node), "{'root':[{'left':[{'left.left':[{},{}]},{}]},{'right':[{},{}]}]}")
        self.assertEqual(serialize(node.left), "{'left':[{'left.left':[{},{}]},{}]}")
        self.assertEqual(serialize(node.right), "{'right':[{},{}]}")

    def test_deserialize(self):
        s = "{'root':[{'left':[{'left.left':[{},{}]},{}]},{'right':[{},{}]}]}"
       
        self.assertEqual(deserialize(s).left.left.val, 'left.left')
        self.assertEqual(deserialize(s).left.val, 'left')
        self.assertEqual(deserialize(s).right.val, 'right')

if __name__ == '__main__':
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    s = "{'root':[{'left':[{'left.left':[{},{}]},{}]},{'right':[{},{}]}]}"

    print(serialize(node))
    print(deserialize(s))

    unittest.main()