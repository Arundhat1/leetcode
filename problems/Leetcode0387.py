class Solution:
    def firstUniqChar(self, s: str) -> int:
        map_count = {}
        
        for i,char in enumerate(s):
            if char in map_count.keys():
                map_count[char] += 1
            else:
                map_count[char] =  1
            
        for i,char in enumerate(s):
            if map_count[char] == 1:
                return i
        return -1
        
