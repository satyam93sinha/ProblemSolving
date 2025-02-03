#User function Template for python3
class Solution:

    def findSubsets(self, pos, remaining_sum, arr, dp, n):
        if pos >= n:
            return int(
                remaining_sum == 0)  # Return 1 if we found a valid subset

        if dp[pos][remaining_sum] != -1:
            return dp[pos][remaining_sum]  # Return the already computed value

        # Exclude the current element
        ans = self.findSubsets(pos + 1, remaining_sum, arr, dp, n)

        # Include the current element if it can be part of the sum
        if arr[pos] <= remaining_sum:
            ans += self.findSubsets(pos + 1, remaining_sum - arr[pos], arr, dp,
                                    n)

        dp[pos][remaining_sum] = ans  # Store the result in dp table
        return ans

    def perfectSum(self, arr, target):
        n = len(arr)
        # Create a dp array initialized to -1 for memoization
        dp = [[-1] * (target + 1) for _ in range(n + 1)]
        # Start recursion with position 0 and the target sum
        return self.findSubsets(0, target, arr, dp, n)

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