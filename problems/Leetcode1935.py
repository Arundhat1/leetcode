class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        words = text.split(" ")
        word_count = len(words)
        for word in words:
            for chara in word:
                if chara in broken:
                    word_count -= 1
                    break
            
        return word_count
