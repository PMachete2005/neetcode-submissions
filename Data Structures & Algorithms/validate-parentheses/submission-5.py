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
                    if chars == ")":
                        if arr[-1] != "(":
                            return False
                    elif chars == "]":
                        if arr[-1] != "[":
                            return False
                    else:
                        if arr[-1] != "{":
                            return False
                else:
                    return False 
                arr.pop() 
        if arr:
            return False
        return True
