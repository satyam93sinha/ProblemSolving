class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        next_greater = self.next_greater(prices)
        difference = [next_greater[index] - prices[index] for index in range(len(prices))]
        return max(difference)
    
    def next_greater(self, prices: List[int]) -> List[int]:
        stack = []
        next_greater_element = [-1 for _ in range(len(prices))]
        for index in range(len(prices)-1, -1, -1):
            while stack and prices[index] >= stack[-1]:
                stack.pop()
            if not stack:
                next_greater_element[index] = prices[index]
                stack.append(prices[index])
            else:
                next_greater_element[index] = stack[-1]
            
            if prices[index] >= stack[-1]:
                stack.append(prices[index])
        
        return next_greater_element