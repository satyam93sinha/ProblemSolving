class Solution:
    def intToRoman(self, num: int) -> str:
        int_to_roman_list = [["I", 1], ["IV", 4], ["V", 5],
                            ["IX", 9], ["X", 10], ["XL", 40],
                            ["L", 50], ["XC", 90], ["C", 100],
                            ["CD", 400], ["D", 500], ["CM", 900],
                            ["M", 1000]]
        
        roman_numeral = ""
        for roman, integer in reversed(int_to_roman_list):
            # 400 // 1000 => 0, 1200 // 1000 = 1
            if num // integer:
                quotient = num // integer
                roman_numeral += (roman * quotient)
                # reduce the num to remainder because we have
                # already considered its quotient in roman conversion
                num %= integer
        
        return roman_numeral