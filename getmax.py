def get_max(n):
    if len(n) == 1:
        return n[0]
    else:
        return max(n[0], get_max(n[1:]))
        
print(get_max([1, 2, 3, 4, 5]))
