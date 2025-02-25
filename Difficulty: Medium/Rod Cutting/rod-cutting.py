#User function Template for python3

class Solution:
    def cutRod(self, price):
        #code here
        dp = {}
        
        def rod_cut(n):
            if n <= 0:
                return 0
            if n in dp:
                return dp[n]
            max_price = price[n-1]
            for length in range(1, n+1):
                max_price = max(max_price,
                                price[length-1] + rod_cut(n-length))
            
            dp[n] = max_price
            return max_price
        
        return rod_cut(len(price))


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):
        # n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a))

        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends