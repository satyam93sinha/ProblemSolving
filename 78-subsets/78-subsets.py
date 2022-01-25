"""
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

"""



class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        def dfs(input_, current_output):
            if not input_:
                output.append(current_output.copy())
            else:
                # include
                current_output.append(input_[0])
                dfs(input_[1:], current_output)
                current_output.pop()
                
                # exclude
                dfs(input_[1:], current_output)
        dfs(nums, [])
        return output
                