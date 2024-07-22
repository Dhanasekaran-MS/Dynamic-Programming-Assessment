# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         # temperatures is the list of temperature for each day
#         # initialize the result
#         n = len(temperatures)
#         result = []
#         # take a day's temperrature
#         for i in range(n):
#             cur = temperatures[i]
#             wait = 0
#             # look for the days we should wait for the temperature which is greater than today
#             for temp in temperatures[i+1:]:
#                 wait+=1
#                 if temp > cur:
#                     # store the no of days
#                     result.append(wait)
#                     wait = 0
#                     break
#             else:
#                 wait = 0
#                 result.append(0)
#         return result
            
def dailyTemperatures(temperatures):
    n = len(temperatures)
    result = [0] * n
    stack = []
    for i in range(n-1,-1,-1):
        while stack and temperatures[i] >= temperatures[stack[-1]]:
            stack.pop()
        if stack:
            result[i] = stack[-1] -i
        stack.append(i)
    return result
        
        
print(dailyTemperatures([73,74,75,71,69,72,76,73]))