# -*- coding: utf-8 -*-

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        tmp = num % 9
        if tmp == 0 and num != 0:
            tmp = 9

        return tmp

if __name__ == '__main__':
    sol = Solution()
    print sol.addDigits(11)
