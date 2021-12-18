"""
Q1. How can we store water?
->> It can be stored in a container, container has dips/depths.
Q2. What is a container?
->> A container has left and right boundary forming a dip in the middle for storage
Q3. How to form left and right boundary?
->> Heights towards left and right will be greater than current height
Q4. What can be the storage if we find left and right boundaries?
->> Storage = min(left boundary, right boundary) - current height
because, current height is like a solid pillar which can not store water in it.

Q5. How to find total storage of rain water in multiple containers?
->> Sum the storage of rain water in single container leading to summation of water stored in all the containers.

Edge Cases:
1. all the heights are same, water will overflow, no water can be stored because there will be no container formed
2. heights is in descending order, water will overflow
3. heights is in ascending order, water will overflow
4. normal case when water can be stored, dips would be formed
"""



class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = -1  # to keep account of max towards left
        max_right = -1  # to keep track of max towards right
        max_left_heights = []  # store max left for every height in heights array
        max_right_heights = []  # store max right for every height
        
        # find maximum left height for every height we encounter
        for index, height_ in enumerate(height):
            max_left = max(max_left, height_)
            max_left_heights.append(max_left)
        
        # find maximum right height for every height
        for index in range(len(height)-1, -1, -1):
            max_right = max(max_right, height[index])
            max_right_heights.append(max_right)
        
        max_right_heights.reverse()
        
        # find the container height for which water will not overflow
        container_height = []
        for left, right in zip(max_left_heights, max_right_heights):
            container_height.append(min(left, right))
        
        # find total storage of water by summing up water storage in every container
        total_storage = 0
        for container, curr_height in zip(container_height, height):
            total_storage += container - curr_height
        
        return total_storage
        