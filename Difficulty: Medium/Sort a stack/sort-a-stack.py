class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def Sorted(self, s):
        # Code here
        if len(s) <= 1:
            return s
        
        last_element = s.pop()
        s = self.Sorted(s)
        s = self.sort_stack(s, last_element)
        return s
    
    def sort_stack(self, s, last_element):
        # base condition
        if len(s) == 0 or s[-1] <= last_element:
            s.append(last_element)
            return s
        
        val_pop = s.pop()
        s = self.sort_stack(s, last_element)
        s = self.sort_stack(s, val_pop)
        return s



#{ 
 # Driver Code Starts

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.Sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(), end=" ")
        print()


# } Driver Code Ends