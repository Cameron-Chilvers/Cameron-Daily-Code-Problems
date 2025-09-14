## Success, Used double linked list since do not know the type of the data, not the best solution, a list would suffice, need to ask questions


# Good morning! Here's your coding interview problem for today.

# This problem was asked by Twitter.

# You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
# You should be as efficient with time and space as possible.




# It could just be a list?

# what datatype is the order id and will it change?

# how many is the expected log number? 5 10, 20000

# how far back would u be trying to find? only 1 or two, or would u want to find the first one?

# do you want it to always be in memory or would you want to store it on disk later?

# will it be resized later?

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = 0
        self.next = 0


def get_pointer(node:Node, nodes: dict[int, Node]) -> int:
    found = None
    for i, val in nodes.items():
        if val == node:
            found = i
            break

    return found

def dereference_pointer(index: int, nodes: dict[int, Node]) -> Node:
    return nodes[index]


class DoubleLinkedList:
    def __init__(self):
        self.heap: dict[int, Node] = {}
        self.head_addr = 0
        self.tail_addr = 0 
        self.length = 0

    def record(self, order_id):
        node = Node(order_id)
        addr = len(self.heap) + 1
        
        if self.head_addr == 0:
            self.head_addr = addr
        else:
            node.prev = self.tail_addr # set new node to the end

            # Point prev node to new node
            old_end_node = dereference_pointer(self.tail_addr, self.heap)
            old_end_node.next = addr
            self.heap[self.tail_addr] = old_end_node

        self.tail_addr = addr
        self.heap[addr] = node
    
    def _traverse_front(self, addr, steps):
        if steps == 0:
            return self.heap[addr].val

        return self._traverse_front(self.heap[addr].next, steps-1)

    def _traverse_back(self, addr, steps):
        if steps == 0:
            return self.heap[addr].val

        return self._traverse_back(self.heap[addr].prev, steps-1)

    def get_last(self, i):
        if i < 1:
            raise Exception("Index has to be above 0")
        
        return self._traverse_back(self.tail_addr, i-1)

class OrderLog:
    def __init__(self, N: int):
        self.buffer = [None] * N
        self.N = N 
        self.index = 0
        self.size = 0
    
    def record(self, order_id):
        self.buffer[self.index] = order_id
        self.index = (self.index + 1) % self.N
        self.size = min(self.size + 1, self.N)

    def get_last(self, i):
        if i < 1 or i > self.N:
            raise Exception("Wrong index number")

        pos = (self.index - i) % self.N
        return self.buffer[pos]



if __name__ == "__main__":
    ids = [1,2,3,4,5]

    dll = DoubleLinkedList()
    for id in ids:
        dll.record(id)

    print(dll.get_last(1))

    log = OrderLog(5)
    for order in [1, 2, 3, 4, 5, 6, 7]:
        log.record(order)

    print(log.get_last(1))  # 7 (most recent)
    print(log.get_last(5))  # 3 (5th most recent)
        
    