#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def nextGreaterElement(self, N, arr):
        # Code here
        stack = []
        next_greater = []
        
        for num in arr[::-1]:
            stack.append(num)
        
        for index in range(N-1, -1, -1):
            while stack and stack[-1] <= arr[index]:
                stack.pop()
            
            if stack:
                next_greater.append(stack[-1])
            else:
                next_greater.append(-1)
            
            stack.append(arr[index])
        
        next_greater.reverse()
        return next_greater

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.nextGreaterElement(N, arr)
        for val in res:
            print(val, end = ' ')
        print()
# } Driver Code Ends