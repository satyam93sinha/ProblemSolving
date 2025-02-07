
from typing import List


class Solution:
    def countPartitions(self, arr, d):
        # code here
        count = 0
        total_sum = sum(arr)
        dp = [[-1 for _ in range(total_sum+1)] for _ in range(len(arr)+1)]
        
        def recur(n, s1):
            # base condition
            if n == 0:
                if 2*s1 - total_sum == d and s1 >= total_sum-s1:
                    return 1
                return 0
            if dp[n][s1] != -1:
                return dp[n][s1]
            ans = recur(n-1, s1)
            if arr[n-1] <= s1:
                ans += recur(n-1, s1-arr[n-1])
            
            dp[n][s1] = ans
            return ans
        
        return recur(len(arr), total_sum)
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.countPartitions(A, D)
        print(ans)
        print("~")

# } Driver Code Ends