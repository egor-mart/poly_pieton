numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

none_element = numbers.index(None)
numbers[none_element] = 0
average_numbers = sum(numbers) / len(numbers)
numbers[none_element] = average_numbers
print(numbers)
