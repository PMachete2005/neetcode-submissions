class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        wordptr = 0
        abbrptr = 0 
        while abbrptr < len(abbr) and wordptr < len(word):
            if abbr[abbrptr] == "0":
                return False
            elif ord(abbr[abbrptr]) > 48 and ord(abbr[abbrptr]) <= 57:
                inttoappend = 0
                while abbrptr < len(abbr) and ord(abbr[abbrptr]) >= 48 and ord(abbr[abbrptr]) <= 57:
                    inttoappend *= 10 
                    inttoappend += int(abbr[abbrptr])
                    abbrptr += 1
                wordptr += inttoappend
                if wordptr > len(word):
                    return False
            else:
                if abbr[abbrptr] == word[wordptr]:
                    abbrptr += 1
                    wordptr += 1
                else:
                    return False
        print(wordptr, abbrptr)
        if wordptr == len(word) and abbrptr == len(abbr):
            return True 
        else:
            return False
            


        