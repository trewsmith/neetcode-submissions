# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 0, n 
        while l <= r: 
            if guess(l + (r - l) // 2) == 0: 
                return l + (r - l) // 2
            elif guess( l + (r - l) // 2) == -1: 
                r =  (l + (r - l) // 2) - 1
                
            else: 
                l =  (l + (r - l) // 2) + 1
                
        
        