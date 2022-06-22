

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s or len(s) == 0:
            return 0
        flag = '+'
        index = 0
        answer = '0'
        if (s[0] == '-' or s[0] == '+'):
            flag = s[0]
            index += 1
        while index < len(s):
            if s[index].isdigit():
                answer += s[index]
                index += 1
            else:
                break
        answer = int(answer)
        if flag == '-':
            answer *= -1
        
        min_ = max_ = pow(2, 31)
        min_ *= -1
        max_ -= 1
        if answer < min_:
            return min_
        elif answer > max_:
            return max_
        return answer
        