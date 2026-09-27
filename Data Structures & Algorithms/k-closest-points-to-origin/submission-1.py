import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            distance = -(pow(point[0], 2) + pow(point[1], 2))
            curtuple = [distance, point]
            if len(heap) < k:
                heapq.heappush(heap, curtuple)
            else:
                heapq.heappushpop(heap, curtuple)
        returnlist = []
        for ele in heap:
            returnlist.append(ele[1])
        return returnlist

        