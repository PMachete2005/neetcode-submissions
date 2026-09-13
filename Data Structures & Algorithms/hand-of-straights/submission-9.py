class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand = sorted(hand)
        myMap = {}
        for i in range(len(hand)):
            if hand[i] in myMap:
                myMap[hand[i]] += 1 
            else:
                myMap[hand[i]] = 1 
        print(myMap)
        i = 0
        numgroups = len(hand) // groupSize
        for x in range(numgroups):
            for j in range(groupSize):
                if (hand[i] + j) in myMap and myMap[hand[i] + j] > 0:
                    myMap[hand[i] + j] -= 1
                else:
                    return False
            while i < len(hand) and myMap[hand[i]] == 0:
                i += 1
        return True

