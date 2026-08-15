class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                # terminate once at a non-9
                return digits

            digits[i] = 0
        # if we end at a 9:
        return [1] + digits