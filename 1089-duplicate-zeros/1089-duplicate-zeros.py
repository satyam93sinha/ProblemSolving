"""
Edge Cases:
1. arr is empty; not possible, a constraint
2. len(arr) == 1; return arr, we can not duplicate 0 in single-lengthed array, so whatever the element be we can return the array itself
3. len(arr) >= 2;
    i) all the elements of arr are 0; return the arr
    ii) first half elements of the arr are 0; after duplication of 0s, arr will only contain 0s
    iii) second half elements of the arr are 0; return the arr, even after duplication, arr would stay as it is because we have to duplicate  0s towards the end
    iv) all the 0s present in the arr can be duplicated
    v) some 0s present in the arr can be duplicated whereas some/last can not be due to limited space/length of the arr
    vi) arr doesn't contain any 0
    
Test Cases:
1. []
2. [2], [0] etc ; return [2], [0]
3. i) [0, 0, 0] ; return [0, 0, 0]
   ii) [0, 0, 0, 1, 2, 3] ; return [0, 0, 0, 0, 0, 0]
   iii) [1, 2, 3, 0, 0, 0] ; return [1, 2, 3, 0, 0, 0]
   iv) [1, 0, 2, 0, 3, 4] ; return [1, 0, 0, 2, 0, 0]
   v) [1, 0, 3, 0, 4] ; return [1, 0, 0, 3, 0]
   vi) [1, 2, 3, 4] ; return [1, 2, 3, 4]
"""

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        possible_duplicates = 0
        length = len(arr) - 1
        # going left to right 
        # and counting zeros to be considered for duplication
        # why considering whole length of array and not leaving last element?
        # Ans:=> in this case last element could be zero and if we don't iterate over the whole array we would end up duplicating it in the next iteration as we would miss not considering the last element for no-duplication
        for left in range(length + 1):
            # left goes beyond allowed elements, stop iteration
            if left > length - possible_duplicates:
                break
            
            # count zeros
            if arr[left] == 0:
                # edge case: don't include the last element which can not be duplicated due to no more space available in the array
                if left == length - possible_duplicates:
                    # move this zero to the end of the array
                    arr[length] = arr[left]  # or 0
                    length -= 1  # we don't have to consider placing this element to its correct position because we already did so
                    break  # break out of the loop, we have already visited and seen all the elements that could be part of resulting arr, we don't have to calculate this 0 too.
                possible_duplicates += 1
        
        last_index = length - possible_duplicates
        # going right to left and placing elements at their correct index
        # also, duplicating zeros
        for right in range(last_index, -1, -1):
            if arr[right] == 0:
                arr[right + possible_duplicates] = arr[right]  # or 0
                # decrement zero
                possible_duplicates -= 1
                arr[right + possible_duplicates] = arr[right]  # or 0, duplicating zero
            
            else:
                arr[right + possible_duplicates] = arr[right]
        