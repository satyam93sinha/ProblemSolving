#User function Template for python3
class Solution:
    def perfectSum(self, arr, target):
        n = len(arr)
        # Create a DP table with (n+1) rows and (target+1) columns
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        
        # Base case: If the target is 0, there's one empty subset that sums to 0
        dp[0][0] = 1
        
        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(target + 1):
                # If the current element is not included
                dp[i][j] = dp[i - 1][j]
                # If the current element is included
                if arr[i - 1] <= j:
                    dp[i][j] += dp[i - 1][j - arr[i - 1]]
        
        # The answer will be in dp[n][target]
        return dp[n][target]





#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tc = int(input().strip())  # Number of test cases
    while tc > 0:
        arr = list(map(int, input().strip().split()))  # Read array input
        target = int(input().strip())  # Read the target sum
        ob = Solution()  # Create the Solution object
        print(ob.perfectSum(arr, target))  # Call perfectSum with 2 arguments
        tc -= 1  # Decrease test case count
        print("~")
# } Driver Code Ends