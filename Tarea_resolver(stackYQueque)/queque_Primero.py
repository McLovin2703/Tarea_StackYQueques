class Solution(object):
    def firstUniqChar(self, s):
        for char in s:
            if s.count(char) == 1:
                return s.index(char)

        return -1