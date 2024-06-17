#User function Template for python3
import math

class Solution:
    def sieveOfEratosthenes(self, N):
    	#code here 
    	prime_numbers = [True for i in range(N+1)]
    	# 0 and 1 are non-prime numbers
    	prime_numbers[0] = prime_numbers[1] = False
    	
    	result = []
    	
    	# iterate from 2 to N
    	for num in range(2, math.ceil(math.sqrt(N+1))):
    	    # mark every prime number's multiple as False
    	    if prime_numbers[num]:
    	        multiple = 2
    	        while num * multiple <= N:
    	            prime_numbers[num*multiple] = False
    	            multiple += 1
    	# print(prime_numbers)
    	
    	for num in range(2, N+1):
    	    if prime_numbers[num]:
    	        result.append(num)
    	    
    	return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sieveOfEratosthenes(N)
        for i in ans:
            print(i, end=" ")
        print()
# } Driver Code Ends