class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda distance: math.sqrt((0-distance[0])**2 + (0-distance[1])**2))[:k]