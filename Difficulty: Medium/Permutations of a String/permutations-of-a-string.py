#User function Template for python3

class Solution:
    def __init__(self):
        self.result = []
        
    def findPermutation(self, s):
        # Code here
        s_list = list(s)
        s_list.sort()
        self.permutations(s_list, 0)
        self.result.sort()
        return self.result
        
    
    def permutations(self, s, index):
        if index == len(s)-1:
            self.result.append(''.join(s))
            return
        seen = set()
        for i in range(index, len(s)):
            if s[i] not in seen:
                seen.add(s[i])
                s[index], s[i] = s[i], s[index]
                self.permutations(s, index+1)
                s[index], s[i] = s[i], s[index]
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        S = input()
        ob = Solution()
        ans = ob.findPermutation(S)
        ans.sort()
        for i in ans:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends