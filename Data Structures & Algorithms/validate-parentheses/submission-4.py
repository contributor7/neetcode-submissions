'''
UPI:
U: check if open parentheses have a matching closing in the order of parentheses recieved
P: thus, need a stack and a hashmap of the parentheses pairs
    quit early if we find a closing parenthesis with no matching open parentheses in the stack
    pop the open parenthesis if the closing one was found
    thus, only put open parentheses in the stack
'''

class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'}' : '{', ']' : '[', ')' : '('}
        stack  = []

        for char in s:
            if char in pairs:
                if len(stack) == 0:
                    return False
                if pairs[char] != stack.pop():
                    return False
            else:
                stack.append(char)
        return len(stack) == 0