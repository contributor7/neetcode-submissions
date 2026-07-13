class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alnum_lower_strippped = ''.join(c.lower() for c in s if c.isalnum())

        for i in range(len(s_alnum_lower_strippped) // 2):
            if s_alnum_lower_strippped[i] != s_alnum_lower_strippped[len(s_alnum_lower_strippped) - 1 - i]:
                return False

        return True

        cleaned = s_alnum_lower_strippped
        return cleaned == cleaned[::-1]

        # cant reverse sort 