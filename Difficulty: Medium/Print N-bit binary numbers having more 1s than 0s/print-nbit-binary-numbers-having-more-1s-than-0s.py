#User function Template for python3
class Solution:
	def NBitBinary(self, n):
		# code here
		answer = []
		ones = zeroes = 0
		out = '1'
		
		def n_bit_bin_nums(out, ones, zeroes, n):
		    if n == 0:
		        answer.append(out)
		        return
		    n_bit_bin_nums(out+'1', ones+1, zeroes, n-1)
		    if zeroes < ones:
		        n_bit_bin_nums(out+'0', ones, zeroes+1, n-1)
		    return
		
		n_bit_bin_nums(out, ones+1, zeroes, n-1)
		return answer


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        ob = Solution()
        answer = ob.NBitBinary(n)
        for value in answer:
            print(value, end=" ")
        print()
        print("~")

# } Driver Code Ends