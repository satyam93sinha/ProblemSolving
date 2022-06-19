#User function Template for python3
class Solution:

	def findMaximum(self,arr, n):
		# code here
		# array is completely sorted
		if arr[-1] > arr[-2]:
		    return arr[-1]
		left, right = 0, n-1
		while left <= right:
		    mid = (left + right) // 2
		    if arr[mid-1] < arr[mid] > arr[mid+1]:
		        return arr[mid]
		    elif arr[mid] < arr[mid+1]:
		        left = mid + 1
		    else:
		        right = mid - 1

#{ 
#  Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaximum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends