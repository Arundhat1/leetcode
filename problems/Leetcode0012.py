class Solution:
    def intToRoman(self, num: int) -> str:
        Sym_val = {
            1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
            10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
            100: 'C', 400: 'CD', 500: 'D', 900: 'CM',
            1000: 'M'
        }
        
        int_rom = ''
        i = 3  # thousands → hundreds → tens → ones
        while i >= 0:
            place_value = 10**i
            dig_place = num // place_value

            if dig_place * place_value in Sym_val:
                int_rom += Sym_val[dig_place * place_value]
            elif dig_place < 4:
                int_rom += Sym_val[place_value] * dig_place
            elif dig_place < 9:
                int_rom += Sym_val[5 * place_value] + Sym_val[place_value] * (dig_place - 5)

            num %= place_value
            i -= 1

        return int_rom
