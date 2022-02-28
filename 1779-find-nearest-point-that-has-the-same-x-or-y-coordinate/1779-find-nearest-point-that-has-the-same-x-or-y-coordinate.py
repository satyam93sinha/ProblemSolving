class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        index = -1  # index of smallest distance points
        smallest_distance = float("inf")  # maintaining the smallest distance
        for curr_index, point in enumerate(points):
            x2, y2 = point
            if x2 == x or y2 == y:  # valid points
                current_distance = abs(x-x2) + abs(y-y2)  # computing distance
                # update only if we have any smaller distance
                if smallest_distance > current_distance:
                    index = curr_index
                    smallest_distance = current_distance
        return index