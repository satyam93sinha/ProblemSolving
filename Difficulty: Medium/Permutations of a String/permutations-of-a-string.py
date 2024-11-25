#User function Template for python3

class Solution:
    def __init__(self):
        self.result = []

    def findPermutation(self, s):
        # Code here
        s = ''.join(sorted(s))
        op = ''
        self.permute(s, op)
        return self.result
    
    def permute(self, inp_s, op):
        if len(inp_s) == 0:
            self.result.append(op)
            return
        seen = set()
        for index in range(len(inp_s)):
            if inp_s[index] not in seen:
                seen.add(inp_s[index])
                new_inp_s = inp_s[:index] + inp_s[index+1:]
                new_op = op + inp_s[index]
                # print(f"new inp:{new_inp_s}, new_op:{new_op}, seen:{seen}")
                self.permute(new_inp_s, new_op)
        



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