class Solution:
    def isHappy(self, n: int) -> bool:

        def sum_digits_squared(n):
            total = 0
            while n:
                digit = n % 10
                total += digit * digit
                n //= 10
            return total


        slow, fast = n, sum_digits_squared(n)

        while slow != fast:
            slow = sum_digits_squared(slow)
            fast = sum_digits_squared(fast)
            fast = sum_digits_squared(fast)
        return slow == 1