class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        column_number_dict = {chr(alphabet_ascii): alphabet_ascii-ord('A')+1 for alphabet_ascii in range(65, 91)}
        # print("Column number dict:", column_number_dict)
        
        column_number = 0
        for index, char in enumerate(columnTitle[::-1]):
            column_number += column_number_dict[char] * pow(26, index)
        
        return column_number