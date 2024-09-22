#User function Template for python3

class Solution:
    def lenOfLongSubarr (self, nums, n, k) : 
        #Complete the function
        end = 0
        curr_sum = 0
        window_size = 0
        prefix_sum_dict = {}
    
        while end < len(nums):
            curr_sum += nums[end]
    
            if curr_sum == k:
                window_size = max(window_size, end + 1)
            elif curr_sum - k in prefix_sum_dict:
                window_size = max(window_size, end - prefix_sum_dict[curr_sum-k])
                
            
            if curr_sum not in prefix_sum_dict:
                prefix_sum_dict[curr_sum] = end
    
            end += 1
            
        return window_size



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, k = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))




# } Driver Code Ends