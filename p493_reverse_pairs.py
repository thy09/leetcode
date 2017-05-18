#! encoding=utf-8

# Creation Date: 2017-04-03 15:04:49
# Created By: Heyi Tang

import random
MAX_INT = 2147483647
#MAX_INT = 100

class BSTNode(object):

    def __init__(self, value):
        self.count = 1
        self.value = value
        self.lchild = None
        self.rchild = None
        self.fix = random.randint(0, MAX_INT)

class Treap(object):

    def __init__(self):
        self.root = None

    def count(self):
        return self.root.count
    
    def update_count(self, node):
        total = 1
        for child in [node.lchild, node.rchild]:
            if child is not None:
                total += child.count
        node.count = total

    def rotate_right(self, node):
        lc = node.lchild
        node.lchild = lc.rchild
        lc.rchild = node
        self.update_count(node)
        return lc

    def rotate_left(self, node):
        rc = node.rchild
        node.rchild = rc.lchild
        rc.lchild = node
        self.update_count(node)
        return rc

    def insert_to_node(self, node, new_node):
        if new_node.value < node.value:
            if node.lchild is None:
                node.lchild = new_node
            else:
                node.lchild = self.insert_to_node(node.lchild, new_node)

            if node.lchild.fix < node.fix:
                node = self.rotate_right(node)
        else:
            if node.rchild is None:
                node.rchild = new_node
            else:
                node.rchild = self.insert_to_node(node.rchild, new_node)

            if node.rchild.fix < node.fix:
                node = self.rotate_left(node)
        self.update_count(node)
        return node

    def insert(self, value):
        new_node = BSTNode(value)
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
                    result += node.rchild.count
                node = node.lchild
            else:
                node = node.rchild
        return result
    
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
            print num, count
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
    maxn = 10000
    dups = 2
    data = []#range(50000)
    for i in range(maxn):
        data.extend([-i] * dups)
        data.extend([i] * dups)
    #data.reverse()
    random.shuffle(data)
    data = json.load(open("nums.in"))
    #print len(data)
    print solu.reversePairs(data)
    fout = open("input.txt","w")
    fout.write("\n".join(map(str,data)))
