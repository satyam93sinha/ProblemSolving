class Solution:
    def average(self, salary: List[int]) -> float:
        sum_salary = sum(salary)
        min_salary = min(salary)
        max_salary = max(salary)
        avg = (sum_salary - min_salary - max_salary) / (len(salary)-2)
        return avg