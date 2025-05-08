#User function Template for python3

class Solution:

    def longestKSubstr(self, s, k):
        # code here
        char_freq = {}
        start = end = 0
        length = -1
        
        while end < len(s):
            char = s[end]
            char_freq[char] = char_freq.get(char, 0) + 1
            if len(char_freq) < k:
                end += 1
            elif len(char_freq) == k:
                length = max(length, end-start+1)
                end += 1
            else:
                while start < end and len(char_freq) > k:
                    char_freq[s[start]] -= 1
                    if char_freq[s[start]] == 0:
                        char_freq.pop(s[start])
                    start += 1
                end += 1
        
        return length


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

        print("~")
# } Driver Code Ends