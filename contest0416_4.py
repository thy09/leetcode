#! encoding=utf-8

# Creation Date: 2017-04-16 09:56:38
# Created By: Heyi Tang


class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod = 1000000007
        result = [[0,0,0, 0,0,0] for i in range(n+5)]
        result[0] = [1, 0, 0, 0, 0, 0]
        for i in range(1, n+1):
            result[i][0] = result[i-1][0] + result[i-1][1] + result[i-1][2] #last is 'P'
            result[i][0] = result[i][0] % mod
            result[i][1] = result[i-1][0] #last is L
            result[i][2] = result[i-1][1] # last is LL
            result[i][3] = result[i-1][0] + result[i-1][1] + result[i-1][2] # last is 'A'
            result[i][3] += result[i-1][3] + result[i-1][4] + result[i-1][5] #last is 'P'
            result[i][3] = result[i][3] % mod
            result[i][4] = result[i-1][3]
            result[i][5] = result[i-1][4]
        for i in range(n):
            print result[i+1], sum(result[i+1])
        final = sum(result[n]) % mod
        return final

if __name__ == "__main__":
    solu = Solution()
    print solu.checkRecord(10)
