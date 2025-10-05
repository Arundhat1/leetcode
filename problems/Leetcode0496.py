class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        max_stack = []
        map_nge = {}
        n = len(nums2)
        for i in range(n):
            num = nums2[n-1-i]
            if max_stack:
                while max_stack and num > max_stack[-1]:
                    max_stack.pop()
                if max_stack:
                    map_nge[num] = max_stack[-1]
                else:
                    map_nge[num] = -1
                max_stack.append(num)
            else:
                map_nge[num] = -1
                max_stack.append(num)
        ans = []
        for j  in nums1:
            ans.append(map_nge[j])
        return ans

