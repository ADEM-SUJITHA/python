def square_numbers(n):
    """
    This function takes a number 'n' and returns a list containing the squares of all numbers from 1 to n. 
    """
    squares = []
    for num in range(1, n + 1):
        squares.append(num ** 2)
    return squares 

# Example usage:
result = square_numbers(5)
print(result) 