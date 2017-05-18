#! encoding=utf-8

# Creation Date: 2017-04-09 09:57:52
# Created By: Heyi Tang

class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = map(int,list(str(n)))
        length = len(digits)
        pos = length - 2
        for i in xrange(length-1):
            if digits[pos] < digits[pos+1]:
                break
            pos -= 1
        if pos == -1:
            return -1
        cur_digit = digits[pos]
        cur_min = 10
        for i in xrange(pos + 1, length):
            if digits[i] <= cur_digit:
                continue
            if digits[i] < cur_min:
                cur_min = digits[i]
                swap_pos = i
        #print digits, pos, swap_pos
        temp = digits[swap_pos]
        digits[swap_pos] = digits[pos]
        digits[pos] = temp
        new_digits = digits[:pos+1] + sorted(digits[pos+1:])
        return int("".join(map(str,new_digits)))

if __name__ == "__main__":
    solu = Solution()
    inputs = [21, 12, 1234567, 7654123, 1, 1234765, 12348621]
    for input in inputs:
        print input, solu.nextGreaterElement(input)
