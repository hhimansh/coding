# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        stx = str(x)
        #reversing a string using slicing
        rev_stx = stx[::-1]
        if stx == rev_stx:
            return True
        else:
            return False