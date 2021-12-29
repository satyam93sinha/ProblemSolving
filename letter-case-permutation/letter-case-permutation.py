"""
Edge Cases:
1. String does not contain alphabets
2. All the char of string are in lowercase
3. All the char of string are in uppercase
4. Normal case, char of string are mixed cases and may be mixed char

Approaches:
1. Brute Force => 
Time: O(n * 2**n) first generate 2**n possibilities then, check valid ones by iterating over string and checking the combinations. 
Space: O(2**n)
Generate all the permutations with and without case change then somehow check for permutations that have characters in same order and case changed or not changed and return them as output.

2. Optimised Approach =>
Time: O(2**n) in worst case, O(2**(len(char))) in strings
Space: O(2**n) if we consider the output array's space

Create a recursive tree handling the base cases when index reaches the end of string or string goes empty and when the char being checked is not an alphabet. Two Choices: Either do not change the case or change the case!
"""



class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        def case_permutation(index=0, result=''):
            # base case 1: index == length
            if index == len(s):
                output.append(result)
            elif not s[index].isalpha():
                # base case 2: char is not an alphabet, its case can't be changed
                case_permutation(index + 1, result + s[index])
            else:
                # the char is an alphabet
                # do not change the case
                case_permutation(index + 1, result + s[index])
                # change the case based on character's current case
                if s[index].isupper():
                    case_permutation(index + 1, result + s[index].lower())
                else:
                    case_permutation(index + 1, result + s[index].upper())
            return output
        
        output = []
        return case_permutation()