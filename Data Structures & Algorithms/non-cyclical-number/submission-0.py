class Solution:
    def isHappy(self, n: int) -> bool:

        hash_set = set()

        while n != 1 and n not in hash_set:

            hash_set.add(n)

            sum = 0

            for v in str(n):
                sum += int(v) ** 2

            n = sum

        return n == 1