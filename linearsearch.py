def linear_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index  # Target found, return its index
    return -1  # Target not found, return -1

# Example usage
arr = [4, 2, 7, 1, 9, 3]
target = 7
result = linear_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the array")
