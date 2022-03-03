class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for customer in range(len(accounts)):
            current_wealth = sum(accounts[customer])
            max_wealth = max(max_wealth, current_wealth)
        
        return max_wealth