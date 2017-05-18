#! encoding=utf-8

# Creation Date: 2017-03-30 23:55:55
# Created By: Heyi Tang

class Solution(object):
    char_list = list("abcdefghijklmnopqrstuvwxyz")
    def next_word(self, word):
        chars = list(word)
        for i in range(len(chars)):
            original = chars[i]
            for c in self.char_list:
                if original == c:
                    continue
                chars[i] = c
                yield "".join(chars)
            chars[i] = original

    def gen_result(self, lastWord, word, beginWord):
        temp = []
        while word != beginWord and word in lastWord:
            temp.append(word)
            word = lastWord[word]
            #print word
        result = [beginWord]
        for i in range(len(temp)):
            result.append(temp[-i-1])
        return result

    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if not endWord in wordList:
            return []
        visited = {}
        dists = {}
        for word in wordList:
            visited[word] = False
            dists[word] = len(wordList) + 1

        lastWord = {}

        from collections import deque
        searchQueue = deque()
        searchQueue.append((beginWord, 0, [beginWord]))
        result = len(wordList) + 1
        results = []
        while searchQueue:
            cur_word, dist, cur_result = searchQueue.popleft()
            print "searching", cur_word, dist
            if dist >= result:
                break
            for word in self.next_word(cur_word):
                if word == endWord:
                    lastWord[endWord] = cur_word
                    result = dist + 1
                    results.append(cur_result + [endWord])
                   # results.append(self.gen_result(lastWord, endWord, beginWord))
                    break
                if not word in dists:
                    continue
                if dists[word] <= dist:
                    continue
                searchQueue.append((word, dist + 1, cur_result + [word]))
                lastWord[word] = cur_word
                visited[word] = True
        return results

if __name__ == "__main__":
    begin = "hit"
    end = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    solu = Solution()
    print solu.findLadders(begin, end, wordList)
    wordList = ["ted","tex","red","tax","tad","den","rex","pee"]
    begin = "red"
    end = "tax"
    print solu.findLadders(begin, end, wordList)
