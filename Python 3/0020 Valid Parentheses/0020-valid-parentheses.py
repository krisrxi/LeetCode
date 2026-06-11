class Solution:
    def isValid(self, s: str) -> bool:

        h = {"(":")", "{":"}", "[":"]"}
        stack = []

        for symbol in s:
            if symbol in h.keys():
                stack.append(symbol)
            elif stack == [] or symbol != h[stack.pop()]
                return False

        return open == []