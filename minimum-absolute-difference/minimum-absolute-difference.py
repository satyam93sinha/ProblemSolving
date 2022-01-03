class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        # print("array sorted:", arr)
        # now, the adjacent elements would result in min absolute diff
        answer = [] # keeping it as a stack
        current_diff = prev_diff = -1
        for index in range(0, len(arr)-1):
            current_diff = abs(arr[index+1] - arr[index])
            if answer:
                prev_diff = abs(answer[-1][1] - answer[-1][0])
            while answer and prev_diff > current_diff:
                answer.pop()
                if answer:
                    prev_diff = abs(answer[-1][1] - answer[-1][0])
                else:
                    prev_diff = -1
            # print(f"current diff:{current_diff}, prev diff:{prev_diff}")
            if not answer or current_diff == prev_diff:
                answer.append([arr[index], arr[index+1]])
                # print("answer appended:", answer)
        return answer