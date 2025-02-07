#User function Template for python3
class Solution:
	def minDifference(self, arr):
		# code here
		n = len(arr)
		total_sum = sum(arr)
		ROWS, COLS = n+1, total_sum+1
		bottom_up = [[False for _ in range(COLS)] for _ in range(ROWS)]
		
		for row in range(ROWS):
		    bottom_up[row][0] = True
		
		for row in range(1, ROWS):
		    for col in range(1, COLS):
		        if arr[row-1] <= col:
		            bottom_up[row][col] = bottom_up[row-1][col-arr[row-1]] or bottom_up[row-1][col]
		        else:
		            bottom_up[row][col] = bottom_up[row-1][col]
		
		min_difference = float("inf")
		
		for col in range(COLS-1, -1, -1):
		    if bottom_up[-1][col]:
		        min_difference = min(min_difference, abs(2*col - total_sum))
		
		return min_difference
		
		
#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.minDifference(arr)
        print(ans)
        tc -= 1
        print("~")

# } Driver Code Ends