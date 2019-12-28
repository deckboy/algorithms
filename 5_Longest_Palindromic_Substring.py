class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        arr_2d = [[False for _ in range(length)] for _ in range(length)]

        max_sub_len = 0
        substring = (0, 0)

        # Trivial case
        for i in range(length):
            arr_2d[i][i] = True

        for i in range(length - 1):
            j = i + 1
            arr_2d[i][j] = s[i] == s[j]
            if arr_2d[i][j] and (2 > max_sub_len):
                max_sub_len = 2
                substring = (i, j)

        step = 2
        for i in range(length - 2):
            i = 0
            j = i + step
            while (i < length) and (j < length):
                arr_2d[i][j] = (s[i] == s[j] and arr_2d[i + 1][j - 1])
                if arr_2d[i][j] and (j - i + 1 > max_sub_len):
                    max_sub_len = j - i + 1
                    substring = (i, j)
                i += 1
                j += 1
            step += 1
        return s[substring[0]:substring[1] + 1]
