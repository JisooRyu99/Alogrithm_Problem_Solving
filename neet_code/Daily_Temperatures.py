# 브루트포스
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        current_temperatures = 0
        
        for i in range(len(temperatures)):
            current_temperatures = temperatures[i]
            flag = False
            cnt = 1
            for j in range(i+1, len(temperatures)):
                
                if current_temperatures < temperatures[j]:
                    print(current_temperatures, temperatures[j], cnt)
                    result.append(cnt)
                    flag=True
                    break
                else:
                    cnt+=1
            if not flag:
                result.append(0)

        return result


# O(n)으로 해결
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                prev = stack.pop()
                result[prev] = i-prev
            
            stack.append(i)
        
        return result
