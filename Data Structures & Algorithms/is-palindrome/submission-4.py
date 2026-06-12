class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = 0
        backwards = len(s) - 1
        boolean = False
        for i in range((len(s) // 2) + 1):
            if ord(s[front]) and ord(s[backwards]):
                boolean = False
                if ord(s[front]) not in range(48, 58):
                    if ord(s[front]) not in range(65, 123):
                        front += 1
                        boolean = True
                if ord(s[backwards]) not in range(48, 58):
                    if ord(s[backwards]) not in range(65, 123):
                        backwards -= 1
                        boolean = True
                if boolean:
                    continue
                else:
                    if s[front] == s[backwards]:
                        front += 1
                        backwards -= 1
                        continue
                    else:
                        if ((ord(s[front]) + 32) == ord(s[backwards])) or ((ord(s[front]) - 32) == ord(s[backwards])):
                            if ord(s[front]) in range(48, 58):
                                if ord(s[backwards]) in range(65, 123):
                                    return False
                            if ord(s[front]) in range(65, 123):
                                if ord(s[backwards]) in range(48, 58):
                                    return False
                            front += 1
                            backwards -= 1
                            continue
                        else:
                            return False
        return True
            

                
