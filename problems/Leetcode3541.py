class Solution:
    def maxFreqSum(self, s: str) -> int:
        max_vowel = 0
        max_conso = 0
        vowels = {'a': 0,"e":0,"i":0,"o":0,"u":0}
        conso = {}
        for chara in s:
            if chara not in vowels.keys():
                if chara not in conso.keys():
                    conso[chara] = 1
                else:
                    conso[chara] +=1
            else:
                vowels[chara] += 1
        if len(conso.keys()) != 0:
            return max(conso.values()) + max(vowels.values())
        else:
            return max(vowels.values())
        
