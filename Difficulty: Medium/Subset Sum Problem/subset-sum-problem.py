#User function Template for python3

class Solution:
    def isSubsetSum (self, arr, target):
        # code here 
        cache = {}
        
        def subset_sum(n, target):
            if (n, target) in cache:
                return cache[(n, target)]
            if target == 0:
                return True
            if n == 0:
                return False
            if arr[n-1] <= target:
                cache[(n, target)] = subset_sum(n-1, target-arr[n-1])
                if cache[(n, target)]:
                    return True
            cache[(n, target)] = subset_sum(n-1, target)
            return cache[(n, target)]
        
        return subset_sum(len(arr), target)
            
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        N = len(arr)
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(arr, sum) == True:
            print("true")
        else:
            print("false")

        print("~")

# } Driver Code Ends