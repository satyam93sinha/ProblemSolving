#User function Template for python3


class Solution:
    def missingNumber(self,array,n):
        # code here
        xor = 0
        for num in array:
            xor ^= num
        
        for index in range(1, n+1):
            xor ^= index
        
        return xor

#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().missingNumber(a,n)
    print(s)
# } Driver Code Ends