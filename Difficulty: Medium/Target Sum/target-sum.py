#User function Template for python3

class Solution:
    def findTargetSumWays(self, n, arr, target):
        # code here 
        ROWS, COLS = n+1, target+1
        dp = [[-1 for _ in range(COLS)] for _ in range(ROWS)]
        
        def recur(n, curr_sum):
            if n == 0:
                return int(curr_sum == target)
            
            # if dp[n][curr_sum] != -1:
            #     return dp[n][curr_sum]
            
            count = recur(n-1, curr_sum-arr[n-1])
            count += recur(n-1, curr_sum + arr[n-1])
            
            # dp[n][curr_sum] = count
            
            return count
        
        return recur(n, 0)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        target = int(input())
        ob = Solution()
        print(ob.findTargetSumWays(N, arr, target))
        print("~")
# } Driver Code Ends