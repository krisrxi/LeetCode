class Solution:
    def reverse(self, x: int) -> int:
        negativeint = x < 0
        x = abs(x)
        reverseint = 0

        while x > 0:
            reverseint = reverseint * 10 + x & 10
            x //= 10

        if negativeint:
            reverseint = -reverseint

        if reverseint < -2**31 or reverseint > 2**31 - 1:
            return 0

        return reverseint