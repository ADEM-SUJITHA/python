def list_sum(numbers):
    if not numbers:
        return 0
    return numbers[0]+list_sum(numbers[1:])
print(list_sum([1,2,3,4,5]))
print(list_sum([10,12.5,10,7]))