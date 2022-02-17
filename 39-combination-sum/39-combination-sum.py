"""
Edge Cases:
1. Single length candidates array
    i) Target sum is found
    ii) Target sum is not found
2. Target sum is not found
3. Target sum is found; return all the combinations

Approaches:
1. Brute Force Using Recursion
Time: O(2^n) We have two choices for every element of candidates, either to include or exclude them in the combination
Space: O(n) max call stack space occupied will be len(candidates)
Intuition: 
Design a Recursive Tree using I/P-O/P Method and then code. Maintain a current_sum, current_result and if current_sum equals target, we have current_result as a subsequence fulfilling the condition.
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def combination_subset(index=0, current_output=[], current_sum=0):
            # base conditions
            # 1. if sum == target
            if current_sum == target:
                output.append(current_output.copy())
                return
            # 2. if current_sum > target, we can never find the target bcoz
            # here the array contains only positive numbers
            if current_sum > target:
                return
            # 3. to ensure we do not go beyond len(candidates)
            # to avoid IndexError
            if index >= len(candidates):
                return
            
            # Hypothesis
            # include same number infinite number of times without ...
            # incrementing index and add it to sum
            current_output.append(candidates[index])
            combination_subset(index, current_output,
                              current_sum + candidates[index])
            current_output.pop()
            
            # exclude the current index, do not add it to current_output
            # increment index so that the next element can be added to ..
            # current_output and sum in the next recursion ...
            # including this candidate infinite number of times as above
            combination_subset(index+1, current_output, current_sum)
    
        output = []
        combination_subset()
        return output
        
        