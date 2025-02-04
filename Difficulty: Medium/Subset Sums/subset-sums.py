#User function Template for python3
class Solution:
	def subsetSums(self, arr):
		# code here
		result = []
		
		def recur(n, curr_sum):
		    if n == 0:
		        result.append(curr_sum)
		        return result
		    recur(n-1, curr_sum + arr[n-1])
		    recur(n-1, curr_sum)
		recur(len(arr), 0)
	    return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())  # Number of test cases
    for i in range(T):
        arr = [int(x)
               for x in input().split()]  # Reading array for the test case
        ob = Solution()
        ans = ob.subsetSums(arr)  # Getting the subset sums
        ans.sort()  # Sorting the result

        # Printing the subset sums in space-separated format
        for x in ans:
            print(x, end=" ")
        print("")  # Ensuring new line after each test case

# } Driver Code Ends