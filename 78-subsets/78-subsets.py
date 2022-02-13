"""
Recursive Tree using I/P-O/P method:

                            [1, 2, 3]
                                |
                   -------------------------
                  |                         |
            {} [2,3]                    {[1]} [2, 3]
              |                             |
        -----------              ---------------
       |           |           |                 |
     {} [3]   {[2]} [3]    {[1]} [3]        {[1,2]} [3]
      |         |               |                 |
  ----        -----          -------          ----------
|     |     |       |       |       |        |           |
{}   [3]  [2]      [2,3]   [1]   [1,3]    [1,2]     [1,2,3]


Edge Cases:
1. Empty nums array : handle in base case
2. nums array containing single element
3. nums array containing duplicate elements; a constraint that nums array does not contain any duplicate element

Intuition:
Generate all the powersets and keep appending them to the output list.

How to generate the powersets?
-> We can use recursion seeing we have two choices, one to include the element in current_output being considered and the other to exclude it. Using i/p-o/p method we can design the Recursion Tree as designed above to figure out the subsets we need.

To generate all the subsets:
Time: O(2^n)
Space: O(2^n) bcoz the output array/list contains at most 2^n elements

"""



class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(index=0, current=[]):
            # base condition, index is greater or equal to length
            # to avoid IndexError
            if index >= len(nums):
                output.append(current.copy())
            else:
                # include
                current.append(nums[index])
                # recursively call dfs
                dfs(index+1, current)
                # to exclude, pop the last element
                current.pop()
                
                # exclude
                dfs(index+1, current)
        
        output = []
        dfs()
        return output