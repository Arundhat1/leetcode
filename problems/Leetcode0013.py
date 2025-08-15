class Solution:
    def romanToInt(self, s: str) -> int:
        dicto = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        value = 0
        n = len(s)
        
        for i in range(n):
            if i < n - 1 and dicto[s[i]] < dicto[s[i + 1]]:
                value -= dicto[s[i]]
            else:
                value += dicto[s[i]]
        
        return value

            
                
             
        
