class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort based on start interval
        intervals.sort(key=lambda element: element[0])
        answer = []
        for start, end in intervals:
            if not answer:
                answer.append([start, end])
            else:
                # merge, if prev_end is less than or equal to current start
                prev_end = answer[-1][1]
                if prev_end >= start:
                    answer[-1][1] = max(prev_end, end)
                else:
                    answer.append([start, end])
        
        return answer