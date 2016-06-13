# -*- coding: utf-8 -*-

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        sList = list(s)
        length = len(s)

        for i in range(length / 2):
            tmp = sList[i]
            sList[i] = sList[length - 1 - i]
            sList[length - 1 -i] = tmp

        return ''.join(sList)


if __name__ == '__main__':
    sol = Solution()
    testStr = 'hello'
    print sol.reverseString(testStr)
