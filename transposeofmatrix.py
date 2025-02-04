x=[[12,-1],[4,5],[3,8]]
r=[[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        r[j][i]=x[i][j]

for items in r:
    print(items)