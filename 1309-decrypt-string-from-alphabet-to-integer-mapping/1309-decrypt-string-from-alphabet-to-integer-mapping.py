class Solution:
    def freqAlphabets(self, s: str) -> str:
        a_i_dict = {str(ascii_+1):chr(ord('a') + ascii_) 
                    for ascii_ in range(0, 9)}
        j_z_dict = {str(ascii_+10)+'#':chr(ord('j') + ascii_) 
                    for ascii_ in range(0, 17)}
        output = ''
        index = 0
        while index < len(s):
            if index < len(s)-2 and s[index+2] == '#':
                current_key = s[index: index+3]
                output += j_z_dict[current_key]
                index += 3
            else:                
                output += a_i_dict[s[index]]
                index += 1
        return output
        