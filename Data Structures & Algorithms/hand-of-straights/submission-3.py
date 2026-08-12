class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand = sorted(hand)
        myMap = {}
        for h in hand:
            if h in myMap:
                myMap[h] += 1 
            else:
                myMap[h] = 1
        minimum = hand[0]
        tracker = 0
        for i in range(len(hand) // groupSize):
            for x in range(minimum, minimum + groupSize):
                if x not in myMap or myMap[x] == 0:
                    return False
                else:
                    myMap[x] -= 1
            while tracker < len(hand):
                if myMap[hand[tracker]] > 0:
                    minimum = hand[tracker]
                    break
                else:
                    tracker += 1 
        return True
        
