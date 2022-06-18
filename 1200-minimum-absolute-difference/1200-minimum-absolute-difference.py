class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        stack = []
        minimum = math.inf
        for index in range(1, len(arr)):
            current_min = arr[index] - arr[index-1]
            while stack and current_min < minimum:
                stack.pop()
            if current_min <= minimum:
                stack.append([arr[index-1], arr[index]])
                minimum = current_min
        return stack