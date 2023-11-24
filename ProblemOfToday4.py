def min_jumps_to_end(nums):
    n = len(nums)
    if n <= 1:
        return 0

    if nums[0] == 0:
        return -1

    jumps = 1
    max_reach = nums[0]
    steps = nums[0]

    for i in range(1, n):
        if i == n - 1:
            return jumps

        max_reach = max(max_reach, i + nums[i])
        steps -= 1

        if steps == 0:
            jumps += 1

            if i >= max_reach:
                return -1

            steps = max_reach - i

    return -1  



user_input = input("Enter a list of numbers separated by spaces: ")
list_from_user = [int(x) for x in user_input.split()]

output = min_jumps_to_end(list_from_user)
print(output)
