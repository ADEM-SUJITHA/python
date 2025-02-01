a=input("enter a string:")
print(a[::1])
print(a[::-1])
if(a[::1]==a[::-1]):
    print("palindrome")
else:
    print("not palindrome")