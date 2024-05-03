#User function Template for python3

class Solution:
    #Complete this function
    def power(self, N, R):
        return self.compute_power(N, R) % 1000000007
    
    def compute_power(self,N,R):
        #Your code here
        if R == 0:
            return 1
        pow_ = self.compute_power(N, R//2) % 1000000007
        pow_ *= pow_
        # check if R is even or odd
        if R % 2 == 0:
            return pow_
        else:
            return pow_ * N

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        N=input()
        R=N[::-1]
        
        ob=Solution();
        ans=ob.power(int(N),int(R))
        print(ans)
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends