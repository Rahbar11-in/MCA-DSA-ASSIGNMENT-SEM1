nums = [0, 1, 0, 3, 12]

def move_zeroes(nums):
    position = 0

    for number in nums:
        if number != 0:
            nums[position] = number
            position += 1

    while position < len(nums):
        nums[position] = 0
        position += 1

    return nums

print(move_zeroes(nums))
