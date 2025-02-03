m1=[[1,2],[3,4]]
m2=[[1,2],[3,4]]
r=[[0,0],[0,0]]
for i in range(len(m1)):
    for j in range(len(m2)):
        for k in range(len(m2)):
            r[i][j]=r[i][j]+m1[i][k]*m2[k][j]
    print("product of two matrices")
for items in r:
    print(items)