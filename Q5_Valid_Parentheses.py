def is_valid(s):
    stack = []
    pairs = {")": "(", "}": "{", "]": "["}

    for bracket in s:
        if bracket in "([{":
            stack.append(bracket)
        else:
            if not stack or stack[-1] != pairs[bracket]:
                return False
            stack.pop()

    return len(stack) == 0

print(is_valid("()"))
print(is_valid("()[]{}"))
print(is_valid("(]"))
