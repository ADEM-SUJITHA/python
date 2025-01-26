def checkkey(d,key):
    if key in d:
        print("key is present in a dictionary")
    else:
        print("key is not present in a dictionary")
        d={'a':100,'b':200,'c':300,'d':400,'e':500}
        key=input("enter a key")
        checkkey(d,key)