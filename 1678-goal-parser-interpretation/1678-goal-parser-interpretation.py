class Solution:
    def interpret(self, command: str) -> str:
        index = 0
        output = ''
        while index < len(command):
            if command[index] == 'G':
                output += 'G'
                index += 1
            elif command[index] == '(':
                if command[index+1] == ')':
                    output += 'o'
                    index += 2
                elif (command[index+1] == 'a'
                      and command[index+2] == 'l'
                      and command[index+3] == ')'):
                    output += 'al'
                    index += 4
        return output