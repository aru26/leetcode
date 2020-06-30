class Solution():
    def titleToNumber(self, s):
        if s == "":
            return 0
        Ans = 0
        for i in range(len(s)):
            Ans *= 26
            Ans += ord(s[i]) - ord("A") + 1
        return Ans
