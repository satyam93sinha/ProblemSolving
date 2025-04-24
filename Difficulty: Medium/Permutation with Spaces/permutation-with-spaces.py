#User function Template for python3


class Solution:

    def permutation(self, s):
        # code here
        answer = []
        def permutation_spaces(op, ip):
            nonlocal answer
            if not ip:
                answer.append(op)
                return
            permutation_spaces(op+' '+ip[0], ip[1:])
            permutation_spaces(op+ip[0], ip[1:])
            
        permutation_spaces(s[0], s[1:])
        return answer



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        S = input()
        ans = ob.permutation(S)
        write = ""
        for i in ans:
            write += "(" + i + ")"
        print(write)

        print("~")
# } Driver Code Ends