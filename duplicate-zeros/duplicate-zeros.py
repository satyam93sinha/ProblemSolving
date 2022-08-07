class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        possible_duplicates = 0
        length = len(arr) - 1  # maintaing the indices
        # count zeros that can and needs be duplicated
        for index in range(length + 1):
            # break for loop when length limit is reached
            if index > length - possible_duplicates:
                break
                
            if arr[index] == 0:
                # not accounting if it's last index in consideration
                if index == length - possible_duplicates:
                    # shifting current/last zero which shouldn't be considered for duplication to end
                    arr[length] = 0
                    length -= 1  # so that we don't touch this zero during duplication
                    break  # we don't need to increment zero count if it is last element
                possible_duplicates += 1
        
        last_index = length - possible_duplicates
        
        for index in range(last_index, -1, -1):
            if arr[index] == 0:
                arr[index + possible_duplicates] = 0
                possible_duplicates -= 1
                arr[index + possible_duplicates] = 0
            else:
                arr[index + possible_duplicates] = arr[index]