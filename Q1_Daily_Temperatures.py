temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

def daily_temperatures(temperatures):
    answer = [0] * len(temperatures)
    stack = []

    for i, temp in enumerate(temperatures):
        while stack and temp > temperatures[stack[-1]]:
            index = stack.pop()
            answer[index] = i - index
        stack.append(i)

    return answer

print(daily_temperatures(temperatures))
