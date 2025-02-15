def vowel_count(str):
    count=0
    vowel=set("aeiouAEIOU")
    for alphabet in str:
        if alphabet in vowel:
            count=count+1
            print("no.of items:",count)


str=input("enter a string:")
vowel_count(str)