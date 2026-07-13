class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def sum_digits_squared(n):
            total = 0
            while n:
                digit = n % 10
                total += digit * digit
                n //= 10
            return total

        while n not in seen and n != 1:
            seen.add(n)
            n = sum_digits_squared(n)

        return n == 1