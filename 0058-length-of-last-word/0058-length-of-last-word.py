class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(" ")
        i = len(s) - 1
        while True:
            if len(s[i]) == 0:
                i -= 1
                continue
            return len(s[i])
