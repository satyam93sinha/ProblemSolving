#User function Template for python3
from collections import deque

def printFirstNegativeInteger( A, N, K):
    # code here
    start = end = 0
    negative_nums = deque()
    result = []
    
    while end < N:
        if A[end] < 0:
            negative_nums.append(A[end])
        
        if end - start + 1 < K:
            end += 1
        elif end - start + 1 == K:
            if negative_nums:
                result.append(negative_nums[0])
            else:
                result.append(0)
            
            if negative_nums and A[start] == negative_nums[0]:
                negative_nums.popleft()
                
            end += 1
            start += 1
    
    return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends