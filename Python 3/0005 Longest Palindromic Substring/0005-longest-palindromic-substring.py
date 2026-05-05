class Solution:
    def longestPalindrome(self, s: str) -> str:
        def ispalindrome(left, right):
            nonlocal maxleft, maxright

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > maxright - maxleft + 1:
                    maxleft, maxright = left, right
                left, right = left - 1, right + 1
        
        maxleft = 0
        maxright = 0

        for i in range(len(s)):
            ispalindrome(i, i)
            ispalindrome(i, i + 1)
        
        return s[maxleft : maxright + 1]