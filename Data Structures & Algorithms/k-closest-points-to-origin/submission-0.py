class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import math
        
        distancePointArr = []
        for i in range(len(points)):
            cur = points[i]
            distance = math.sqrt(((cur[0]) ** 2) + ((cur[1]) ** 2))
            distancePointArr.append([distance, cur])
        heapq.heapify(distancePointArr)

        #heapify distancePointArr based on distance
        #pop from the top k times and add just the points to the result array

        res = []
        for _ in range(k):
            res.append(heapq.heappop(distancePointArr)[1])
        
        return res

        