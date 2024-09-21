#User function Template for python3
from collections import deque

class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,arr,k):
        if not len(arr):
            return []
        #code here
        start = end = 0
        result = []
        # keep track of max using a double ended queue
        curr_max_queue = deque()
        
        while end < len(arr):
            # store the curr max element
            while curr_max_queue and curr_max_queue[-1] < arr[end]:
                curr_max_queue.pop()
            curr_max_queue.append(arr[end])
            
            if end - start + 1 < k:
                end += 1
            elif end - start + 1 == k:
                result.append(curr_max_queue[0])
                if arr[start] == curr_max_queue[0]:
                    curr_max_queue.popleft()
                
                start += 1
                end += 1
        
        return result
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n, k = map(int, input().strip().split())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        res = ob.max_of_subarrays(arr, k)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()

# } Driver Code Ends