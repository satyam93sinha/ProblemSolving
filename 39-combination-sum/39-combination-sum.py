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
        
        def combinations(index=0, current_result=[], current_sum=0):
            # base condition
            if current_sum == target:
                output.append(current_result.copy())
                return
            if current_sum > target:
                return
            if index >= len(candidates):
                return
            
            # Hypothesis, searching for subsequences for smaller input
            # by deciding to include or exclude an element and consequently
            # input automatically gets small
            
            # include, we can pick same elements multiple number of times
            current_result.append(candidates[index])
            combinations(index, current_result,
                         current_sum + candidates[index])
            current_result.pop()
            
            # exclude
            combinations(index+1, current_result, current_sum)
            
        output = []
        combinations()
        return output
        
        
        