#User function Template for python3
"""
Edge Cases:
1. txt is empty; return 0, no anagram occurred
2. pat is empty; return 0, no pattern present for which we have to find anagrams
3. pat is found in txt, count number of occurrences of anagrams
    a) txt == pat
    b) txt != pat, len(txt) can or can not be equal to len(pat)
4. pat is not found in txt, return 0

Test Cases:
for
for
orf
for
forxxorfxdofr
for
aabaabaa
aaba
forx
xdf

Approaches:
We have k = len(pat)
1. Brute Force
Intuition:
Iterate outer and inner for loop, check if current dictionary of char matches
that present in pattern
Time: O(n^2)
Space: O(26) to store pattern's frequency and count, alphabets not more than 26

2. Use Sliding Window
Intuition:
Maintain sliding window of size k and increment count of anagrams if it is found
Time: O(n)
Space: O(26)
"""
import collections

class Solution:

	
	def search(self,pat, txt):
	    # code here
	    start, end = 0, 0
	    k = len(pat)
	    n = len(txt)
	    pat_char_freq = collections.Counter(pat)
	    distinct_char = len(pat_char_freq)
	    anagrams = 0

	    while end < n:
	        # calculation
	        if txt[end] in pat_char_freq:
	            pat_char_freq[txt[end]] -= 1
	            if pat_char_freq[txt[end]] == 0:
	                distinct_char -= 1
	        if end - start + 1 < k:
	            end += 1
	        elif end - start + 1 == k:
	            # end - start + 1 == k
	            # ans <- calculation
	            if distinct_char == 0:
	                anagrams += 1
	            # remove start from calculation
	            if txt[start] in pat_char_freq:
	                pat_char_freq[txt[start]] += 1
	                if pat_char_freq[txt[start]] == 1:
	                    distinct_char += 1
	            start += 1
	            end += 1
	    return anagrams

#{ 
#  Driver Code Starts
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