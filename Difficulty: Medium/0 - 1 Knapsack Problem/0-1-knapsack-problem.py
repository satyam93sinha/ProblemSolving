#User function Template for python3

class Solution:
    # Function to return max value that can be put in knapsack of capacity.
    def knapSack(self, capacity, val, wt):
        # code here
        
        cache = {}
        
        def dfs(capacity, index):
            if (capacity, index) in cache:
                return cache[(capacity, index)]
            elif index < 0 or capacity == 0:
                return 0
            elif capacity-wt[index] >= 0:
                cache[(capacity, index)] = max(val[index] + dfs(capacity-wt[index], index-1),
                                            dfs(capacity, index-1))
                return cache[(capacity, index)]
            else:
                return dfs(capacity, index-1)
        
        return dfs(capacity, len(wt)-1)
        


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        # Read capacity
        capacity = int(input())
        values = list(map(
            int,
            input().strip().split()))  # Using 'values' instead of 'val'
        weights = list(map(
            int,
            input().strip().split()))  # Using 'weights' instead of 'wt'
        ob = Solution()
        print(ob.knapSack(capacity, values, weights))
        print("~")

# } Driver Code Ends