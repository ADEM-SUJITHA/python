import array as arr
a=arr.array('i',[1,2,3])
print("array before insertion:",end="")
for i in range(0,3):
    print(a[i],end="")
print( )
a.insert(1,4)
a.append(5)
print("array after insertion:",end="")
for i in a:
    print(i,end=" ")
print( )
a.reverse()
print("reversed array:",*a)
