class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses_dict = {')':'(', '}':'{', ']':'['}
        for char in s:
            if char in {'(', '{', '['}:
                stack.append(char)
            else:
                # stack goes empty or last element of stack is not the one expected from parentheses_dict then parentheses is unbalanced
                if not stack or stack.pop() != parentheses_dict[char]:
                    return False
        
        return False if stack else True