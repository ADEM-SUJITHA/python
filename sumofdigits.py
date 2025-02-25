n = 12345
sum = 0

while n > 0:
    sum += n % 10  # extract last digit
    n //= 10       # remove last digit

print(sum)