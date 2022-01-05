class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        partition = []
        
        def is_palindrome(start, end):
            while start < end:
                if s[start] == s[end]:
                    start += 1
                    end -= 1
                else:
                    return False
            return True
        
        def dfs(index):
            if index >= len(s):
                result.append(partition.copy())
            else:
                for end_index in range(index, len(s)):
                    if is_palindrome(index, end_index):
                        partition.append(s[index: end_index + 1])
                        dfs(end_index + 1)
                        partition.pop()
        
        dfs(0)
        return result
    
                        