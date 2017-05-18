#! encoding=utf-8

# Creation Date: 2017-04-09 10:12:09
# Created By: Heyi Tang

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.longest = 1
        self.deep_search(root)
        return self.longest

    def deep_search(self, node):
        node.lincr = node.ldecr = 0
        if node.left is not None:
            print node.val, " left ", node.left.val
            self.deep_search(node.left)
            if node.val == node.left.val + 1:
                node.lincr = node.left.max_incr
            if node.val == node.left.val - 1:
                node.ldecr = node.left.max_decr

        node.rincr = node.rdecr = 0
        if node.right is not None:
            print node.val, " right ", node.right.val
            self.deep_search(node.right)
            if node.val == node.right.val + 1:
                node.rincr = node.right.max_incr
            if node.val == node.right.val - 1:
                node.rdecr = node.right.max_decr

        node.max_incr = max(node.lincr, node.rincr) + 1
        node.max_decr = max(node.ldecr, node.rdecr) + 1
        print node.max_incr, node.max_decr, "left:", node.lincr, node.ldecr, "right:", node.rincr, node.rdecr, "val:", node.val

        if node.lincr + node.rdecr + 1>self.longest:
            self.longest = node.lincr + node.rdecr + 1
        if node.rincr + node.ldecr + 1> self.longest:
            self.longest = node.rincr + node.ldecr + 1

if __name__ == "__main__":
    root = TreeNode(1)
    n1 = TreeNode(2)
    n2 = TreeNode(3)
    n3 = TreeNode(4)
    root.left = n1
    root.right = n2
    n1.left = n3
    #root.right = n2
    solu = Solution()
    print solu.longestConsecutive(root)
