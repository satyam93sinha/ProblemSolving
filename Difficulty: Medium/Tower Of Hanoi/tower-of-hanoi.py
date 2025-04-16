# User function Template for python3

class Solution:
    def __init__(self):
        self.total_moves = 0
        
    def  towerOfHanoi(self, n, fromm, to, aux):
        # Your code here
        if n == 0:
            return 0
        self.towerOfHanoi(n-1, fromm, aux, to)
        # induction
        self.total_moves += 1
        self.towerOfHanoi(n-1, aux, to, fromm)
        return self.total_moves


#{ 
 # Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while (T > 0):
        N = int(input())
        ob = Solution()
        print(ob.towerOfHanoi(N, 1, 3, 2))
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends