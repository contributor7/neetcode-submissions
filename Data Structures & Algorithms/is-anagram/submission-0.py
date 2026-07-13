class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_list1 = sorted(list(s))
        char_list2 = sorted((t))
        return char_list1 == char_list2