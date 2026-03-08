class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        b_index=-1
        min_seen_cap=float('inf')

        for i in range(len(capacity)):
            if capacity[i]>=itemSize:
                if capacity[i]<min_seen_cap:
                    min_seen_cap=capacity[i]
                    b_index=i

        return b_index