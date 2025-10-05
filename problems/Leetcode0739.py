class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []  # stores indices

        for i, temp in enumerate(temperatures):
            # resolve any days that are cooler than today
            while stack and temperatures[stack[-1]] < temp:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)
        
        return ans
