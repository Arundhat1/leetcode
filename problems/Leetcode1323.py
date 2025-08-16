class Solution:
    def maximum69Number (self, num: int) -> int:
        num_str = str(num)
        max_str = ''
        for i,char in enumerate(num_str):
            if char == '6':
                max_str = num_str[:i] + '9' + num_str[i+1:]
                break
        if max_str == '':
            return num
        
        return(int(max_str))






        
