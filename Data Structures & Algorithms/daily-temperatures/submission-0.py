class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)

        for current_day in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[current_day]:
                prev_day = stack.pop()
                answer[prev_day] = current_day - prev_day

            stack.append(current_day)

        return answer
        