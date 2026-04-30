def calculate_list_statistics(numbers: list[float]) -> tuple[float, float, float, float]:
    """Return total, average, maximum and minimum of a list of numbers."""
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return total, average, maximum, minimum


numbers = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
total, average, maximum, minimum = calculate_list_statistics(numbers)

print("Total:", total)
print("Media:", average)
print("Maior:", maximum)
print("Menor:", minimum)
