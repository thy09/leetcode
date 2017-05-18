#! encoding=utf-8

# Creation Date: 2017-04-03 14:12:52
# Created By: Heyi Tang

class Solution(object):

    def gen_result(self, words, words_width, maxWidth):
        count = len(words)
        space_width = maxWidth - words_width
        if count == 1:
            return words[0] + " " * space_width
        intervals = count - 1
        space_width_right = space_width / intervals
        mod = space_width % intervals
        chars = []
        for i in range(intervals):
            chars.extend(list(words[i]))
            for j in xrange(space_width_right):
                chars.append(" ")
            if i < mod:
                chars.append(" ")
        chars.extend(list(words[intervals]))
        return "".join(chars)

    def gen_last_result(self, words, words_width, maxWidth):
        space_width = maxWidth - words_width
        intervals = len(words) - 1
        space_width -= intervals
        if space_width > 0:
            words.append(" " * (space_width-1))
        return " ".join(words)

    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        cur_width = 0
        cur_words = []
        cur_words_width = 0
        result = []
        for word in words:
            word_width = len(word)
            if cur_width + word_width > maxWidth:
                result.append(self.gen_result(cur_words, cur_words_width, maxWidth))
                cur_width = 0
                cur_words = []
                cur_words_width = 0
            cur_width += word_width + 1
            cur_words_width += word_width
            cur_words.append(word)
        result.append(self.gen_last_result(cur_words, cur_words_width, maxWidth))
        return result
