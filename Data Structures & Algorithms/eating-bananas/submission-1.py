class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minimum = 1
        maximum = max(piles)

        while minimum < maximum:
            mid = (minimum + maximum) // 2
            h_needed = 0

            for pile in piles:
                h_needed += math.ceil(pile/mid)

            if h_needed > h:
                minimum = mid + 1
            else:
                maximum = mid
        return minimum
            