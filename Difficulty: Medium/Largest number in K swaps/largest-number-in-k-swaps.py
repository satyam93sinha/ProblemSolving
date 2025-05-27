#User function Template for python3

class Solution:
    
    #Function to find the largest number after k swaps.
    def __init__(self):
        self.result = float('-inf')
        
    def findMaximumNum(self, s, k):
        #code here
        self.result = int(''.join(s))
        s = list(s)
        self.max_num(s, k, 0)
        return str(self.result)
    
    def max_num(self, s, k, start):
        if k == 0 or start == len(s)-1:
            s_int = int(''.join(s.copy()))
            # print("base condition:", s, s_int)
            self.result = max(self.result, s_int)
            return self.result
        
        # find max in s[start+1:]
        current_max = max(s[start+1:])
        
        # backtrack
        for index in range(start+1, len(s)):
            if s[start] < s[index] and s[index] == current_max:
                s[start], s[index] = s[index], s[start]
                # print("for loop:", s, k, start)
                s_int = int(''.join(s.copy()))
                # print("base condition:", s, s_int)
                self.result = max(self.result, s_int)
                self.max_num(s, k-1, start+1)
                s[start], s[index] = s[index], s[start]
        self.max_num(s, k, start+1)
        
        return self.result
