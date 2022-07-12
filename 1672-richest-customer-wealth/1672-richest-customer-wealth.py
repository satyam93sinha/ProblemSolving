class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum = 0
        for customer in accounts:
            current_amount = 0
            for bank in customer:
                current_amount += bank
            maximum = max(maximum, current_amount)
        return maximum