#! encoding=utf-8

# Creation Date: 2017-04-03 14:25:32
# Created By: Heyi Tang

from p68_text_justify import Solution

if __name__ == "__main__":
    words = ["This", "isis", "anan", "example", "offfffffff", "text", "justif."]
    words = ["is", "is", "is", "is", "is", "is", "is", "is"]
    L = 7
    solu = Solution()
    result = solu.fullJustify(words, L)
    for r in result:
        print "|%s|" % r, len(r)
