# coding: utf-8

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        sList = list(s)
        length = len(s)

        for i in range(length / 2):
            sList[i], sList[length - 1 - i] = sList[length - 1 - i], sList[i]

        return ''.join(sList)


if __name__ == '__main__':
    sol = Solution()
    testStr = 'hello'
    print sol.reverseString(testStr)
