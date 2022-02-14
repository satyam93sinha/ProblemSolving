"""
Edge Cases:
1. Single element; return 0
2. Ascending order; return difference of last element and first one
3. Descending order; return 0
4. Same element throughout the array; return 0

Approaches:
1. Brute Force
Intuition:
Iterate through every element of the array and check for max difference between elements.
Time: O(n^2)
Space: O(1)

2. Use Stack
Intuition:
We iterate backwards and keep the maximum element as we encounter it in stack maintaining a result array storing max_element for that element at that particular location. Later, we find difference between result array and input array then finding the max difference element.
Time: O(n) we iterate 3 times over the array but it will be linear.
Space: O(n) we have a stack which can grow until n-size in worst case

3. Maintain a min_element and max_difference/current_max
Intuition:
We can maintain a min_element as we encounter any minimum element lesser than current_min we update it and keep track of max_difference/max_profit by checking/storing max difference in max_profit.
Time: O(n)
Space; O(1)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_element = prices[0]
        max_profit = 0
        for price in prices:
            # keep track of min_element as we iterate over prices
            if price < min_element:
                min_element = price
            # account for max_profit and keep it updated
            elif max_profit < price-min_element:
                max_profit = max(max_profit, price-min_element)
        
        return max_profit