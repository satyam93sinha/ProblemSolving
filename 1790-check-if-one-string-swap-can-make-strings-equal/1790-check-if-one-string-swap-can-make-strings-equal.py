class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # base condition
        # count of elements are different or any char is different,
        # return False
        if collections.Counter(s1) != collections.Counter(s2):
            return False
        else:
            # count the number of swaps required
            difference = 0
            for s1_char, s2_char in zip(s1, s2):
                if s1_char == s2_char:
                    continue
                else:
                    difference += 1
            return True if difference <= 2 else False