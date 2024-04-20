#User function Template for python3
import math

class Solution:
    def isPrime (self, N):
        # code here
        if N == 1:
            return 0
        elif N == 2:
            return 1
        
        for divisor in range(2, math.ceil(math.sqrt(N))+1):
            if N % divisor == 0:
                return 0
        
        return 1
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.isPrime(N))
# } Driver Code Ends