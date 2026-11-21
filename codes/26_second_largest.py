def second_largest(numbers):
    unique_numbers = []

    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)

    if len(unique_numbers) < 2:
        return None

    largest = unique_numbers[0]
    second = unique_numbers[1]

    if second > largest:
        largest, second = second, largest

    for num in unique_numbers[2:]:
        if num > largest:
            second = largest
            largest = num
        elif num > second:
            second = num

    return second