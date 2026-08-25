class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        leastDiff = 100001
        l, r = 0, k - 1
        while r < len(arr):
            diffSum = 0
            for i in range(l , r + 1):
                diffSum += abs(x - arr[i])
            if diffSum < leastDiff:
                leastDiff = diffSum
                cur = []
                for i in range(l , r + 1):
                    cur.append(arr[i])
            l+=1
            r+=1
        return cur
        