class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        t = set()
        n = len(s)

        for r in range(n):
            while s[r] in t:
                t.remove(s[l])
                l += 1

            window = (r - l) + 1
            longest = max (longest, window)
            t.add(s[r])

        return longest