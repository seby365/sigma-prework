def max_n_min(numbers):
    highest = numbers[0]
    lowest = numbers[0]

    for number in numbers:
        if number > highest:
            highest = number
        if number < lowest:
            lowest = number
    return [lowest, highest]

print(max_n_min([2, 4, 1, 0, 2, -1]))
print(max_n_min([20, 50, 12, 6, 14, 8]))
print(max_n_min([100, -100]))