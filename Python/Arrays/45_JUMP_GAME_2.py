class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        end = 0
        farthest = 0
        
        # Traverse until the second last index
        for i in range(len(nums) - 1):
            # Update farthest reachable index
            farthest = max(farthest, i + nums[i])
            
            # If we reach the end of the current jump range
            if i == end:
                jumps += 1
                end = farthest
                
                # Optimization: if farthest already reaches last index
                if end >= len(nums) - 1:
                    break
        return jumps
