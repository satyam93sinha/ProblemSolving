# User function Template for Python3

class Solution:
    def equalPartition(self, arr):
        # code here
        total_sum = sum(arr)
        if total_sum % 2 != 0:
            return False
        else:
            return self.isSubsetSum(arr, total_sum//2)

    def isSubsetSum (self, arr, target):
        # code here 
        ROWS = len(arr) + 1
        COLS = target + 1
        t = [[False for col in range(COLS)] for row in range(ROWS)]
        
        for row in range(ROWS):
            t[row][0] = True
            
        for row in range(1, ROWS):
            for col in range(1, COLS):
                if arr[row-1] <= col:
                    t[row][col] = t[row-1][col-arr[row-1]] or t[row-1][col]
                else:
                    t[row][col] = t[row-1][col]
        
        return t[ROWS-1][COLS-1]
        

#{ 
 # Driver Code Starts
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        if ob.equalPartition(arr):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends