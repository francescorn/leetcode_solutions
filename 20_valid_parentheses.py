class Solution:
    def isValid(self, s: str) -> bool:
        x = "()"
        y = "[]"
        z = "{}"
        while x in s or y in s or z in s:
            s = s.replace(x, "").replace(y, "").replace(z, "")
        if len(s) == 0:
            s = 0
        return s == 0
