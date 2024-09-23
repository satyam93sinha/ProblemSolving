#User function Template for python3

class Solution:

    def longestKSubstr(self, s, k):
        # code here
        start = end = 0
        unique_char_dict = {}
        window_size = -1
        
        while end < len(s):
            unique_char_dict[s[end]] = end
            
            if len(unique_char_dict) < k:
                end += 1
            elif len(unique_char_dict) == k:
                window_size = max(window_size, end-start+1)
                end += 1
            else:
                while unique_char_dict[s[start]] != start:
                    start += 1
                unique_char_dict.pop(s[start])
                start += 1
                end += 1
        
        return window_size


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