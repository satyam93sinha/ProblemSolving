#User function Template for python3
class Solution:
    def maximumSumSubarray (self,arr,k):
        # code here 
        max_sum = curr_sum = 0
        start = end = 0

        while end < len(arr):
            curr_sum += arr[end]
            if end - start + 1 < k:
                end += 1
            else:
                max_sum = max(max_sum, curr_sum)
                curr_sum -= arr[start]
                start += 1
                end += 1
        return max_sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.maximumSumSubarray(arr, k)
        print(ans)
        tc -= 1
        print("~")

# } Driver Code Ends