#User function Template for python3

class Solution:
    def printTillN(self, N):
    	#code here 
    	if N == 0:
    	    return
    	self.printTillN(N-1)
    	print(N, end=" ")
    	return


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printTillN(N)
        print()
# } Driver Code Ends