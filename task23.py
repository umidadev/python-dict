def group_indices(numbers: list[int]) -> dict[int, list[int]]:
    group = {}

    for idx, num in enumerate(numbers):
        if num not in group:
            group[num] = []
        group[num].append(idx)

    return group


numbers = [4, 6, 8, 3, 4, 6, 1, 2, 5, 6, 2, 3, 4]
result = group_indices(numbers)
print(result)
