class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        closest = float('inf')
        
        for i in range(n-2):
            left, right = i+1, n-1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                
                if abs(s - target) < abs(closest - target):
                    closest = s
                
                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    return target   # exact match
        return closest
