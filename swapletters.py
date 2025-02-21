s = input()
result = ""
i = 0

while i < len(s) - 1:  # Ensures that it doesn't try to access an out-of-bound index
    result += s[i+1] + s[i]
    i += 2

if i < len(s):  # Append the last character if the length of s is odd
    result += s[i]

print(result)
