#User function Template for python3

class Solution:
    def allPalindromicPerms(self, S):
        # code here 
        self.palindromes = []
        self.find_palindromes(S, start=0, palindrome_str=[])
        return self.palindromes
    
    def find_palindromes(self, S, start, palindrome_str) -> None:
        if start >= len(S):
            # print(palindrome_str)
            self.palindromes.append(palindrome_str.copy())
            return
        for index in range(start+1, len(S)+1):
            if self.is_palindrome(S[start:index]):
                palindrome_str.append(S[start:index])
                self.find_palindromes(S, index, palindrome_str)
                palindrome_str.pop()
    
    def is_palindrome(self, string):
        # print("string:", string)
        left, right = 0, len(string)-1
        while left < right:
            if string[left] == string[right]:
                left += 1
                right -= 1
                continue
            else:
                return False
        return True