#User function Template for python3
"""
Edge Cases:
1. empty string, not possible, a constraint
2. K > len(S) --> what to return? -1 because there is no substring with K unique chars
3. K <= len(S)
    a. present, find the longest substring with K unique chars
    b. K unique chars not present, return -1

Test Cases:
S = "abc", K = 4
S = "abc", K = 3
S = "aabacbebebe" K = 3
"""
import collections

class Solution:

    def longestKSubstr(self, s, k):
        # code here
        start = end = 0
        k_char_freq = {}
        longest_substring_len = -1

        while start <= end and end < len(s):
            # calculations
            char = s[end]
            if char in k_char_freq:
                k_char_freq[char] += 1
            else:
                k_char_freq[char] = 1
            # haven't found k unique char yet
            if len(k_char_freq) < k:
                end += 1
            # count_distinct_char == k, found k unique char
            elif len(k_char_freq) == k:
                # ans <- calculation
                longest_substring_len = max(longest_substring_len, end-start+1)
                
                end += 1
            else:
                while start <= end and len(k_char_freq) > k:
                    k_char_freq[s[start]] -= 1
                    if k_char_freq[s[start]] == 0:
                        k_char_freq.pop(s[start])
                    start += 1
                end += 1
        
        return longest_substring_len
            
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()
        k = int(input())

        solObj = Solution()

        ans = solObj.longestKSubstr(s, k)

        print(ans)

# } Driver Code Ends