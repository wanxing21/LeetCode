# -*- coding: utf-8 -*-

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0

if __name__ == '__main__':
    sol = Solution()
    print sol.canWinNim(4)
