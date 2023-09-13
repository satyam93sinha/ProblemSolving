#User function Template for python3
class Solution:
    def findKRotation(self,arr,  n):
        # code here
        left, right = 0, n-1
        while left <= right:
            mid = (left + right) // 2
            if (mid == 0 or arr[mid-1] > arr[mid]) and (mid == n-1 or arr[mid] < arr[mid+1]):
                return mid
            # sorted or not
            if arr[left] < arr[mid]:
                if arr[mid] < arr[right]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if arr[mid] < arr[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	tc=int(input())
	while tc > 0:
		n=int(input())
		a=list(map(int , input().strip().split()))
		ob = Solution()
		ans=ob.findKRotation(a, n)
		print(ans)
		tc=tc-1



# } Driver Code Ends