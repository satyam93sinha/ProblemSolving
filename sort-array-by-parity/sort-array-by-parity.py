class Solution(object):
    def sortArrayByParity(self, A):
        odd_num_index = len(A)-1
        even_num_index = 0
        while even_num_index < odd_num_index:
            # swap if front has odd num and back has even num
            # (A[even_num_index] % 2) > (A[odd_num_index] % 2)
            if A[even_num_index] % 2 == 1 and A[odd_num_index] % 2 == 0:
                A[even_num_index], A[odd_num_index] = A[odd_num_index], A[even_num_index]
                even_num_index += 1
                odd_num_index -= 1
            
            # front num is an even number
            if A[even_num_index] % 2 == 0:
                even_num_index += 1
            
            # back num is an odd number
            if A[odd_num_index] % 2 == 1:
                odd_num_index -= 1
        
        return A
        
        """
        odd_num_index = 0
        for even_num_index, num in enumerate(A):
            if num % 2 == 0:
                A[odd_num_index], A[even_num_index] = A[even_num_index], A[odd_num_index]
                odd_num_index += 1
        
        return A
        """
        
        """
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 > A[j] % 2:
                A[i], A[j] = A[j], A[i]

            if A[i] % 2 == 0: i += 1
            if A[j] % 2 == 1: j -= 1

        return A
        """