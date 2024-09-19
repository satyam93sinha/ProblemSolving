#User function Template for python3
class Solution:

	
	def search(self,pat, txt):
	    # code here
	    start = end = 0
        anagrams_count = 0
        
        pat_char_count = {}
        for char in pat:
            pat_char_count[char] = pat_char_count.get(char, 0) + 1
        
        distinct_char = len(pat_char_count)
        
        # counting anagrams, use sliding window
        while end < len(txt):
            # calculation
            char = txt[end]
            if char in pat_char_count:
                pat_char_count[char] = pat_char_count.get(char) - 1
                if pat_char_count[char] == 0:
                    distinct_char -= 1
            
            # window size?
            if end - start + 1 < len(pat):
                end += 1
            # answer
            elif end - start + 1 == len(pat):
                if distinct_char == 0:
                    anagrams_count += 1
                if txt[start] in pat_char_count:
                    pat_char_count[txt[start]] = pat_char_count.get(txt[start]) + 1
                    if pat_char_count[txt[start]] == 1:
                        distinct_char += 1
                
                # slide window
                start += 1
                end += 1
        
        return anagrams_count

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