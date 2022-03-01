class Solution:
    def isHappy(self, n: int) -> bool:
        hashset = set()
        while n != 1 and n > 0:
            hashset.add(n)
            square_sum = 0
            while n > 0:
                square_sum += pow(n % 10, 2)
                n //= 10
            n = square_sum
            if n in hashset:
                return False
        return True