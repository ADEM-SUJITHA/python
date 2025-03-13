def Reverse( s ):
    result = ""
    n = 0
    start = 0
    while ( s[n:] != "" ):
        while ( s[n:] != "" and s[n] != ' ' ):
            n = n + 1
            result = s[ start: n ] + " " + result
            start = n
    return result