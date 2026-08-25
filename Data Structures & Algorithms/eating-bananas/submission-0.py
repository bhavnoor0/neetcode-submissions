class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        min_k = right

        while left <= right:
            mid = (right + left)//2
            mid_hours = 0
            for pile in piles:
                mid_hours += ((pile - 1)) // mid + 1
            if mid_hours <= h:
                min_k = min(mid, min_k)
                right = mid - 1
            else:
                left = mid + 1
        return min_k