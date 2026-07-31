class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1count = [0] * 26 
        s2count = [0] * 26
        for i in range(len(s1)):
            s1count[ord(s1[i]) - ord('a')] += 1
            s2count[ord(s2[i]) - ord('a')] += 1
        matches = 0 
        for i in range(26):
            if s1count[i] == s2count[i]:
                matches += 1 
        if matches == 26:
            return True
        left = 0 
        right = left + len(s1)
        while right < len(s2):
            if s2count[ord(s2[left]) - ord('a')] == s1count[ord(s2[left]) - ord('a')]:
                matches -= 1
            else:
                if (s2count[ord(s2[left]) - ord('a')] - 1) == s1count[ord(s2[left]) - ord('a')]:
                    matches += 1
            s2count[ord(s2[left]) - ord('a')] -= 1 
            left += 1
            if s2count[ord(s2[right]) - ord('a')] == s1count[ord(s2[right]) - ord('a')]:
                matches -= 1
            else:
                if (s2count[ord(s2[right]) - ord('a')] + 1) == s1count[ord(s2[right]) - ord('a')]:
                    matches += 1
            s2count[ord(s2[right]) - ord('a')] += 1
            right += 1
            if matches == 26:
                return True
        return False


        