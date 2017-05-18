#! encoding=utf-8

# Creation Date: 2017-04-08 00:28:05
# Created By: Heyi Tang
from collections import defaultdict

def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    mod = a % b
    if mod == 0:
        return b
    return gcd(b, mod)

class Solution(object):
    def simplify(self, dx, dy):
        divider = gcd(dx,dy)
        return "%d/%d" % (dx/divider, dy/divider)

    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        points.sort(key = lambda p:p.x)
        count = len(points)
        if count < 3:
            return count
        max_num = 2
        visited = [False] * count
        for i in xrange(count-2):
            if visited[i]:
                continue
            base = points[i]
            print "i=",i, base.x, base.y
            nums = defaultdict(int)
            num = 1
            for j in xrange(i+1, count):
                dx = points[j].x - base.x
                dy = points[j].y - base.y
                if dx == 0 and dy == 0:
                    num += 1
                    print i, j, num
                    visited[j] = True
                    continue
                key = self.simplify(dx, dy)
                val = nums[key] + 1
                print key, dx, dy, val
                nums[key] = val
                if val + num > max_num:
                    max_num = val + num
            if num > max_num:
                max_num = num
                print "update", num, max_num
            if count - i <= max_num:
                break
        return max_num

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

if __name__ == "__main__":
    points = []
    for i in range(5):
        for j in range(5):
            points.append(Point(3*(15-i+2),2*(i*i+1)))
    solu = Solution()
    print solu.maxPoints(points)
