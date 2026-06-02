class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        i, direction = 0, 1
        rows = [[] for _ in range(numRows)]

        for char in s:
            rows[i].append(char)
            if i == 0:
                direction = 1
            elif i == numRows - 1:
                direction = -1
            i += direction

        for i in range(numRows):
            rows[i] = "".join(rows[i])

        return "".join(rows)