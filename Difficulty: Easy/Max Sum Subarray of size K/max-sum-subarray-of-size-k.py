#User function Template for python3
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        # code here 
        start = end = 0
        max_sum = float('-inf')
        curr_sum = 0
        
        while end < N:
            curr_sum += Arr[end]
            
            if end - start + 1 < K:
                end += 1
            elif end - start + 1 == K:
                max_sum = max(max_sum, curr_sum)
                curr_sum -= Arr[start]
                start += 1
                end += 1
        
        return max_sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends