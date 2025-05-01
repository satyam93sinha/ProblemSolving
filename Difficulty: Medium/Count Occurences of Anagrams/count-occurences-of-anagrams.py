#User function Template for python3
class Solution:

	
	def search(self,pat, txt):
	    # code here
	    k = len(pat)
	    pat_dict = {}
	    for char in pat:
	        pat_dict[char] = pat_dict.get(char, 0) + 1
	    
	    start = end = 0
	    count = len(pat_dict)
	    anagrams = 0
	    
	    while end < len(txt):
	        # calculation
	        char = txt[end]
	        if char in pat_dict:
	            pat_dict[char] -= 1
	            if pat_dict[char] == 0:
	                count -= 1
	        if end - start + 1 < k:
	            end += 1
	        else:
	            # answer <- calculation
	            if count == 0:
	                anagrams += 1
	            
	            if txt[start] in pat_dict:
	                pat_dict[txt[start]] += 1
	                if pat_dict[txt[start]] == 1:
	                    count += 1
	            
	            start += 1
	            end += 1
	    return anagrams


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
        print("~")
# } Driver Code Ends