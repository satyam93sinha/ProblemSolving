class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda element: element[0])
        answer = []
        for start, end in intervals:
            if not answer:
                answer.append([start, end])
            else:
                if start <= answer[-1][1]:
                    answer[-1][1] = max(end, answer[-1][1])
                else:
                    answer.append([start, end])
        return answer