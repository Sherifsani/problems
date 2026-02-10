class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        low, high = 2, x // 2 # Square root of x (where x > 1) is never more than x/2
        
        while low <= high:
            mid = (low + high) // 2
            sqr = mid * mid
            
            if sqr == x:
                return mid
            elif sqr < x:
                low = mid + 1
            else:
                high = mid - 1
                
        # When the loop ends, high is the floor of the square root
        return high