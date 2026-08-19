class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}

        for ch in s:
            seen[ch] = seen.get(ch, 0) + 1

        for i in range(len(s)):
            m = s[i]

            if seen[m] == 1:
                return i

        return -1