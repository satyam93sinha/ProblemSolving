"""
Problem Statement Observations:
1. N number of books given, has Ai pages in them
2. sorted in ascending order -> max pages of books is A[-1]
3. Allocate contiguous books to M students
4. 0/1 knapsack kind, can not divide the pages of a book, each book assigned to one student
5. each student should be allocated at least 1 book
6. Contiguous order

Edge Cases:
1. M students > len(A) number of books available to be allocated; return -1
2. M students == len(A); return max of A
3. M Students < len(A)
    3.1 books can be allocated to students or it can not be

Approaches:
1. Brute Force
Intuition:

"""


class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self,A, N, M):
        #code here
        # edge case1
        if M > N:
            return -1
        if M == N:
            return max(A)
        
        left, right = max(A), sum(A)
        result = -1
        while left <= right:
            mid = (left + right) >> 1
            if self.is_valid(A, N, M, mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result
    
    def is_valid(self, array, length, students, max_):
        allocated_students = 1
        pages = 0
        for index in range(length):
            if pages + array[index] > max_:
                allocated_students += 1
                pages = 0
            pages += array[index]
        
        if allocated_students > students:
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