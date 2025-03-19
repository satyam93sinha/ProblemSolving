class Solution:
    def __init__(self):
        self.dp = {}
    def knapsack(self, W, val, wt):
        # code here
        self.dp = [[-1 for _ in range(W+1)] for _ in range(len(wt)+1)]
        return self.knapsack_0_1(len(wt), W, val, wt)
    
    def knapsack_0_1(self, n, W, val, wt):
        if self.dp[n][W] != -1:
            return self.dp[n][W]
        if n == 0 or W == 0:
            return 0
        if wt[n-1] <= W:
            self.dp[n][W] = max(val[n-1] + self.knapsack_0_1(n-1, W-wt[n-1], val, wt),
                        self.knapsack_0_1(n-1, W, val, wt))
        else:
            self.dp[n][W] = self.knapsack_0_1(n-1, W, val, wt)
        
        return self.dp[n][W]



#{ 
 # Driver Code Starts
if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        capacity = int(input())
        values = list(map(int, input().strip().split()))
        weights = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.knapsack(capacity, values, weights))
        print("~")
# } Driver Code Ends