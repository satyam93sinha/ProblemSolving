#User function Template for python3
class Solution:

	
	def search(self,pat, txt):
	    # code here
	    pat_counter = [0 for _ in range(26)]
	    for char in pat:
	        pat_counter[ord(char) - ord('a')] += 1
	       
	    start = end = 0
	    occurences = 0
	    txt_counter = [0 for _ in range(26)]
	    
	    while end < len(txt):
	        # calculation
	        txt_counter[ord(txt[end]) - ord('a')] += 1
	        
	        if end - start + 1 < len(pat):
	            end += 1
	        elif end - start + 1 == len(pat):
	            # answer <-- calculation
	            if txt_counter == pat_counter:
	                occurences += 1
	            # remove first one
	            txt_counter[ord(txt[start]) - ord('a')] -= 1
	            # slide
	            start += 1
	            end += 1
	    
	    return occurences
	            


#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        txt=input().strip()
        pat=input().strip()
        ob = Solution()
        ans = ob.search(pat, txt)
        print(ans)
        tc=tc-1
# } Driver Code Ends