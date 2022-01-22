class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self,A, N, M):
        #code here
        
        
        left, right = max(A), sum(A)
        # print("left:{}, right:{}".format(left, right))
        min_pages = -1
        while left <= right:
            mid = (left + right) // 2
            # print("mid pages:", mid)
            if self.is_valid(A, N, M-1, mid):
                min_pages = mid
                right = mid - 1
                # print("Valid pages, min_pages:{}, mid:{}".format(min_pages, mid))
            else:
                left = mid + 1
            # print("while loop end, left:{}, right:{}".format(left, right))
        return min_pages
        
    def is_valid(self, array, size, students, pages):
        sum_ = 0
        # print("Is Valid, array:{}, students:{}, pages:{}, sum_:{}".format(
        #                                     array, students, pages, sum_))
        for page in array:
            # print("page:", page)
            sum_ += page
            # print("sum_:", sum_)
            if sum_ > pages:
                sum_ = page
                students -= 1
                # print("sum_ > pages, students:", students)
            if students < 0:
                # print("Return False!!")
                return False
        return True
                


#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        m=int(input())
        
        ob=Solution()
        
        print(ob.findPages(arr,n,m))
# } Driver Code Ends