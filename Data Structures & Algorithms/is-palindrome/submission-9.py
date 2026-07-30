class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0 
        end = len(s) - 1 
        while start < end:
            if s[start].isalnum() and s[end].isalnum():
                if s[start].lower() != s[end].lower():
                    return False
            else:
                if s[start].isalnum():
                    end -= 1
                    continue
                elif s[end].isalnum():
                    start += 1
                    continue
            start += 1 
            end -= 1
        return True

       
            

                
