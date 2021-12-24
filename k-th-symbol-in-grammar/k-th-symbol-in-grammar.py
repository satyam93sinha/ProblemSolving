class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1 or k == 1:
            return 0
        else:
            # hypothesis
            kth_element = self.kthGrammar(n-1, math.ceil(k/2))
            
            # induction
            if k % 2 == 0:
                return 1 if kth_element == 0 else 0
            else:
                return kth_element