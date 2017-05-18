#! encoding=utf-8

# Creation Date: 2017-04-03 15:04:49
# Created By: Heyi Tang

import random
MAX_INT = 2147483647
#MAX_INT = 100

class BSTNode(object):

    def __init__(self, value, data = None):
        self.data = data
        self.value = value
        self.lchild = None
        self.rchild = None
        self.parent = None
    
    def append_left(self, node):
        if self.lchild is not None:
            raise Exception
        self.lchild = node
        node.parent = self

    def append_right(self, node):
        if self.rchild is not None:
            raise Exception
        self.rchild = node
        node.parent = self

    def repr(self):
        print self.value, self.data,
        print self.parent, self.lchild, self.rchild
    def show(self, depth = 0, signal = ""):
        print signal, self.value, self.data
        if self.lchild is not None:
            self.lchild.show(depth + 1, signal + "ll")
        if self.rchild is not None:
            self.rchild.show(depth + 1, signal + "rr")

class Treap(object):

    def __init__(self):
        self.root = None

    def depth(self):
        return self.root.data["max_depth"]

    def count(self):
        return self.root.data["count"]

    def update_depth(self, node):
        max_child_depth = 0
        for child in [node.lchild, node.rchild]:
            if child is not None:
                if child.data["max_depth"] > max_child_depth:
                    max_child_depth = child.data["max_depth"]
        node.data["max_depth"] = max_child_depth + 1
    
    def update_count(self, node):
        total = 1
        for child in [node.lchild, node.rchild]:
            if child is not None:
                total += child.data["count"]
        node.data["count"] = total

    def rotate_right(self, node):
        lc = node.lchild
        node.lchild = lc.rchild
        lc.rchild = node
        self.update_depth(node)
        self.update_count(node)
        return lc

    def rotate_left(self, node):
        rc = node.rchild
        node.rchild = rc.lchild
        rc.lchild = node
        self.update_depth(node)
        self.update_count(node)
        return rc

    def insert_to_node(self, node, new_node):
        if new_node.value < node.value:
            if node.lchild is None:
                node.append_left(new_node)
            else:
                node.lchild = self.insert_to_node(node.lchild, new_node)

            if node.lchild.data["fix"] < node.data["fix"]:
                node = self.rotate_right(node)
        else:
            if node.rchild is None:
                node.append_right(new_node)
            else:
                node.rchild = self.insert_to_node(node.rchild, new_node)

            if node.rchild.data["fix"] < node.data["fix"]:
                node = self.rotate_left(node)
        self.update_depth(node)
        self.update_count(node)
        return node

    def insert(self, value):
        data = {"fix": random.randint(0, MAX_INT),
                "max_depth": 1,
                "count": 1,
                }
        new_node = BSTNode(value, data)
        if self.root == None:
            self.root = new_node
            return
        self.root = self.insert_to_node(self.root, new_node)

    def greater_than(self, value):
        node = self.root
        result = 0
        while node is not None:
            if value < node.value:
                result += 1
                if node.rchild is not None:
                    result += node.rchild.data["count"]
                node = node.lchild
            else:
                node = node.rchild
        return result
    
    def show(self):
        if self.root is None:
            return
        self.root.show(0)

class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        treap = Treap()
        total = 0
        for num in nums:
            count = treap.greater_than(2*num)
            #print num, count
            total += count
            treap.insert(num)
        return total

def test_treap():
    values = range(50) * 1000
    #random.shuffle(values)
    treap = Treap()
    for x in values:
        treap.insert(x)
    print treap.depth()
    print treap.count()
    for x in random.sample(values, 10):
        print x, treap.greater_than(x)

import json
if __name__ == "__main__":
    solu = Solution()
    data = range(50000)
    data.reverse()
    data = json.load(open("nums.in"))
    print solu.reversePairs(data)
