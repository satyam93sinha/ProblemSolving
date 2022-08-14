class Solution(object):
    def sortArrayByParity(self, A):
        odd_num_index = 0
        for even_num_index, num in enumerate(A):
            if num % 2 == 0:
                A[odd_num_index], A[even_num_index] = A[even_num_index], A[odd_num_index]
                odd_num_index += 1
        
        return A
        
        """
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 > A[j] % 2:
                A[i], A[j] = A[j], A[i]

            if A[i] % 2 == 0: i += 1
            if A[j] % 2 == 1: j -= 1

        return A
        """