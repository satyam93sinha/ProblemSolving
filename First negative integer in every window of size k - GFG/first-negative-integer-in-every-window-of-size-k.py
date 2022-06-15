#User function Template for python3
import collections

def printFirstNegativeInteger( A, N, K):
    # code here
    start, end = 0, 0
    queue = collections.deque()
    answer = []
    
    while end < N:
        if A[end] < 0:
            queue.append(A[end])
        if end - start + 1 < K:
            end += 1
        else:
            # calculation
            # end - start + 1 == K
            if queue:
                answer.append(queue[0])
            else:
                answer.append(0)
            # remove start from calculation
            if queue and A[start] == queue[0]:
                queue.popleft()
            # slide the window
            start += 1
            end += 1
    
    return answer

#{ 
#  Driver Code Starts
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