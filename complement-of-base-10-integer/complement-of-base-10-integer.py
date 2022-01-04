class Solution:
    def bitwiseComplement(self, n: int) -> int:
        n_bin = bin(n)[2:]
        result_bin = ''
        for char in n_bin:
            if char == '1':
                result_bin += '0'
            else:
                result_bin += '1'
        
        return int(result_bin, 2)