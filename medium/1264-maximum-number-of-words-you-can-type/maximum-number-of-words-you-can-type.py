class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        count = 0

        for word in words:
            if not any(letter in brokenLetters for letter in word):
                count+=1
        return count
        