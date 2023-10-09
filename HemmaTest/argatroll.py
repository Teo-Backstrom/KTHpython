y = []
n  = 5
for i in range(n):
    x = []
    for j in range(n):
        x.append("|_")
    y.append(x)
        
for i in range(n):
    
    for j in range(n):
        print(y[i][j], end="")
    print("|")