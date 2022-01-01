"""
Observe:
n = 2, (()), ()()
Here, n = 2 ==> opening_braces = closing_braces = 2
1. if opening_brackets == closing_brackets; go for opening bracket, only one choice
2. if opening_bracket = 0, only one choice of going with closing bracket
3. else go for opening and closing both choices and decrement respective counts

Base Condition:
1. n == 1, 
opening_braces == 0, append the resultant parentheses to output list and backtrack

Approaches:
1. Brute Force -> 
Time: O(2**n * n) for checking and generating all the parentheses
Space: O(2**n) for storing all the generated parentheses
Generate all the parentheses and then, check which of them is balanced and return them

2. Use Recursion/Backtracking/Make Decisions -> make choices, maintain balanced order of parentheses
Time: O(2**n)
Space: O(2**n)
"""



class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        opening_braces, closing_braces = n, n
        return self.generate_parentheses(opening_braces, closing_braces,
                                        "", [])
        
    def generate_parentheses(self, opening_braces, closing_braces, 
                             result, output):
        # base case
        if opening_braces == 0:
            result += ')'*closing_braces
            output.append(result)
        elif opening_braces == closing_braces:
            # edge case1 => we have only choice to proceed with opening bracket
            # to maintain balanced parentheses, else we will get )( unbalanced
            # parentheses
            result += "("
            self.generate_parentheses(opening_braces-1, closing_braces,
                                     result, output)
        else:
            # two choices,
            # 1. include opening bracket and mantain its balance
            self.generate_parentheses(opening_braces-1, closing_braces,
                                     result+'(', output)
            # 2. include closing bracket and maintain its balance
            self.generate_parentheses(opening_braces, closing_braces-1,
                                     result+')', output)
        return output
            