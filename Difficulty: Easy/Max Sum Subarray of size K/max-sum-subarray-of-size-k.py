#User function Template for python3
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        # code here 
        start = end = 0
        current_sum = 0
        max_sum = -float('inf')
        
        while end < N:
            current_sum += Arr[end]
            
            # calculation, building ans
            if end - start + 1 < K:
                end += 1
            
            elif end - start + 1 == K:
                # found k length window
                max_sum = max(max_sum, current_sum)
                # reduce ans
                current_sum -= Arr[start]
                # slide window
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