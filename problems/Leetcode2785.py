class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')

        sL = list(s)
        vowel_present = []
        for chara in sL:
            if chara not in vowels:
                pass
            else:
                vowel_present.append(chara)
        vowel_present = sorted(vowel_present)

        i = 0
        j = 0
        n = len(sL)
        m = len(vowel_present)
        while i < n:
            if sL[i]  in vowels:
                sL[i] = vowel_present[j]
                j += 1
            else:
                pass
            i += 1
        return "".join(sL)
    


        
