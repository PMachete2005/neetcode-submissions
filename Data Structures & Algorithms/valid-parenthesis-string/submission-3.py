class Solution:
    def checkValidString(self, s: str) -> bool:
        openstack = []
        starstack = []
        for i in range(len(s)):
            if s[i] == "(":
                openstack.append(i)
            if s[i] == "*":
                starstack.append(i)
            if s[i] == ")":
                if len(openstack) > 0:
                    openstack.pop()
                else:
                    if len(starstack) > 0:
                        starstack.pop()
                    else:
                        return False
        if len(openstack) == 0:
            return True
        else:
            while len(openstack) > 0 and len(starstack) > 0:
                if starstack[-1] > openstack[-1]:
                    starstack.pop()
                    openstack.pop()
                else:
                    return False
        if len(openstack) > 0:
            return False
        else:
            return True
