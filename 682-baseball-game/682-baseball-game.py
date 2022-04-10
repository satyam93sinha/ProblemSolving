class Solution:
    def calPoints(self, ops: List[str]) -> int:
        answer = []
        for operation in ops:
            if operation == "+":
                answer.append(answer[-1]+answer[-2])
            elif operation == "C":
                answer.pop()
            elif operation == "D":
                answer.append(2*answer[-1])
            else:
                answer.append(int(operation))
        
        return sum(answer)