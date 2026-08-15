class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) - 1
        num = 0

        for digit in digits:
            num += digit * (10 ** n)
            print(num, digit, n)
            n -= 1
        
        num += 1
        num_str = str(num)

        res = []
        for digit in num_str:
            res.append(digit)
        
        return res