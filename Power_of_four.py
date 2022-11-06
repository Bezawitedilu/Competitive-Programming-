class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        num = n
        while n >= 3:
            num /= 4
            n //= 4
        return True if num == 1 and n > 0 else False
