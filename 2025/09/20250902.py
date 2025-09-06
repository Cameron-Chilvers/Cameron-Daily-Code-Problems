## Half Half, Understood what was meant on the question just need to clarify if ever get a question, e.g. if tail index is accepted


# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

# If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.

import unittest

class Node:
    def __init__(self, data):
        self.data = data
        self.both = 0

    def get_xor_index(self, index):
        return self.both ^ index

    def set_both(self, both):
        self.both = both

    def get_both(self):
        return self.both

def get_pointer(node:Node, nodes: dict[int, Node]) -> int:
    found = None
    for i, val in nodes.items():
        if val == node:
            found = i
            break

    return found

def dereference_pointer(index: int, nodes: dict[int, Node]) -> Node:
    return nodes[index]

class XORLinkedList:
    def __init__(self):
        self.heap: dict[int, Node] = {}
        self.head_addr = 0
        self.tail_addr = 0
    
    def add(self, val):
        node = Node(val)
        addr = len(self.heap) + 1
        
        if self.head_addr == 0:
            node.set_both(0)
            self.head_addr = addr
        else:
            node.set_both(self.tail_addr) # set new node to the end

            # Update old end node
            old_end_node = dereference_pointer(self.tail_addr, self.heap)
            prev_old_end = old_end_node.get_both()
            old_end_node.set_both(prev_old_end ^ addr)
            self.heap[self.tail_addr] = old_end_node

        self.tail_addr = addr
        self.heap[addr] = node

    def traverse_list(self, start, steps, prev) -> Node:
        if steps == 0:
            return dereference_pointer(start, self.heap)

        start_node = dereference_pointer(start, self.heap)
        xor_value = start_node.get_xor_index(prev)
        return self.traverse_list(xor_value, steps-1, start)

    def get(self, index):
        if index+1 > self.tail_addr:
            raise IndexError
        return self.traverse_list(self.head_addr, index, 0)

class Test_Problem(unittest.TestCase):
    def setUp(self):
        self.xor_list = XORLinkedList()
        self.xor_list.add(10)

    def test_add_and_get_first(self):
        self.xor_list.add(20)
        self.xor_list.add(30)
        self.assertEqual(self.xor_list.get(0).data, 10)

    def test_add_and_get_middle(self):
        self.xor_list.add(20)
        self.xor_list.add(30)
        self.xor_list.add(40)
        self.assertEqual(self.xor_list.get(2).data, 30)

    def test_add_and_get_last(self):
        self.xor_list.add(20)
        self.xor_list.add(30)
        self.xor_list.add(40)
        self.assertEqual(self.xor_list.get(3).data, 40)

    def test_out_of_bounds(self):
        self.xor_list.add(20)
        with self.assertRaises(IndexError):
            self.xor_list.get(5)


if __name__ == "__main__":
    # Create the first node (head of the list)
    xor_list = XORLinkedList()
    xor_list.add(10)
    xor_list.add(20)
    xor_list.add(30)
    assert xor_list.get(0).data == 10
    assert xor_list.get(1).data == 20

    unittest.main()