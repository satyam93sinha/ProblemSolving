#User function Template for python3
import math

class Solution:
	def AllPrimeFactors(self, N):
		# Code here
		if N < 2:
		    return []
		answer = set()
		for num in range(2, math.ceil(math.sqrt(N))+1):
		    # check if the number is prime
		    if self.is_prime(num):
		        # prime factors divide the number leaving remainder = 0
		        while N % num == 0:
		            N //= num
		            answer.add(num)
		            answer.add(N)
		    result = []
		    for num in answer:
		        if self.is_prime(num):
		            result.append(num)
		    result.sort()
		return result if result else [N]
	
	def is_prime(self, num):
	    if num < 2:
	        return False
	    if num == 2 or num == 3:
	        return True
	    for divisor in range(2, math.ceil(math.sqrt(num))+1):
	        if num % divisor == 0:
	            return False
	    return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.AllPrimeFactors(N)
		for _ in ans:
			print(_, end = " ")
		print()
# } Driver Code Ends