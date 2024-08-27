#User function Template for python3

from typing import List

class Solution:
    def reverse(self, St):
        #code here
        if len(St) <= 1:
            return St
        val = St.pop()
        self.reverse(St)
        return self.insert(St, val)
    
    def insert(self, St, val):
        if not St:
            St.append(val)
            return St
        popped = St.pop()
        self.insert(St, val)
        St.append(popped)
        return St
        


#{ 
 # Driver Code Starts

#Initial Template for Python 3

 
for _ in range(int(input())):
    N = int(input())
    St = list(map(int, input().split()))
    ob = Solution()
    ob.reverse(St)
    print(*St)
# } Driver Code Ends