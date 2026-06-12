class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = 0
        backwards = len(s) - 1
        mySetmaster = set()
        mySet = set()
        mySetnums = set()
        for i in range(65, 123):
            mySetmaster.add(i)
            mySet.add(i)
        for i in range(48, 58):
            mySetmaster.add(i)
            mySetnums.add(i)
        for i in range((len(s) // 2) + 1):
            if ord(s[front]) not in mySetmaster or ord(s[backwards]) not in mySetmaster:
                if ord(s[front]) not in mySetmaster:
                    front += 1
                if ord(s[backwards]) not in mySetmaster:
                    backwards -= 1
                continue
            else:
                if s[front] == s[backwards]:
                    front += 1
                    backwards -= 1
                    continue
                else:
                    if ((ord(s[front]) + 32) == ord(s[backwards])) or ((ord(s[front]) - 32) == ord(s[backwards])):
                        if (ord(s[front])) in mySetnums and ord(s[backwards]) in mySet:
                            return False
                        elif ord(s[front]) in mySet and ord(s[backwards]) in mySetnums:
                            return False
                        else:
                            print(ord(s[front]))
                            print(ord(s[backwards]))
                            continue
                    else:
                        return False
        return True
            

                
