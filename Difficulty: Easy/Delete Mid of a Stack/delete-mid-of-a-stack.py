#User function Template for python3

class Solution:
    
    #Function to delete middle element of a stack.
    def deleteMid(self, s, sizeOfStack):
        # code here
        if sizeOfStack % 2 == 1:
            return self.pop_mid(s, sizeOfStack//2, sizeOfStack-1)
        else:
            return self.pop_mid(s, sizeOfStack//2 - 1, sizeOfStack-1)
    
    def pop_mid(self, s, mid, index):
        # base condition
        if mid == index:
            s.pop()
            return s
        val = s.pop()
        s = self.pop_mid(s, mid, index-1)
        s.append(val)
        return s


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import sys

sys.setrecursionlimit(10**8)


def main():
    t = int(input())
    while (t > 0):
        sizeOfStack = int(input())
        myStack = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.deleteMid(myStack, sizeOfStack)
        while (len(myStack) > 0):
            print(myStack[-1], end=" ")
            myStack.pop()
        print()
        t -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends