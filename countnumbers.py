string=input("enter a string:")
count=0
string=string.lower()
for i in string:
    if i=='a'or 'e' or 'i' or 'o' or 'u':
     count=count+1
    if count==0:
      print("no vowels found:")
    else:
      print("total vowels are:"+str(count))