#User function Template for python3

class Solution:
    def findPermutation(self, s):
        # Code here
        result = []
        s = ''.join(sorted(s))
        
        def permute(inp, out):
            if not inp:
                result.append(out)
                return
            
            for index in range(len(inp)):
                if index == 0 or inp[index] != inp[index-1]:
                    permute(inp[:index]+inp[index+1:], out+inp[index])
            return
        
        permute(s, '')
        return result



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