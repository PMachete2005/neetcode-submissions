class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        if len(s) < 2:
            return False
        for chars in s:
            if chars == "(" or chars == "[" or chars == "{":
                arr.append(chars)
            else:
                if arr:
                    cur = arr.pop()
                    if chars == ")":
                        if cur != "(":
                            return False
                    elif chars == "]":
                        if cur != "[":
                            return False
                    else:
                        if cur != "{":
                            return False
                else:
                    return False  
        if arr:
            return False
        return True
