class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Brute force: try every speed k from 1 to max(piles)
        max_p = max(piles)
        for k in range(1, max_p + 1):
            hours = 0
            for p in piles:
                # ceil(p / k) without floats
                hours += (p + k - 1) // k
                if hours > h:  # tiny early break; still brute force over k
                    break
            if hours <= h:
                return k
        return max_p  # fallback (always reachable by k = max(piles))