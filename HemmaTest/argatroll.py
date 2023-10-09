
def checksurround(y, x, A):
    if A[y][x] == "|*":
        print("Är samma")
        return True
    for i in range(y-1, y+1):
        for j in range(x-1, x+1):
            if A[i][j] == "|*":
                print("Går inte")
                return True
    
    return False


A = []
n  = 5
for i in range(n):
    x = []
    for j in range(n):
        x.append("|_")
    A.append(x)
        
for i in range(n):
    
    for j in range(n):
        print(A[i][j], end="")
    print("|")
    
val = input("Val")
while val != "ö":
    
    y, x = val.split(" ")
    y = int(y) - 1
    x = int(x) - 1
    while(checksurround(y,x,A)):
        val = input("Val")
        y, x = val.split(" ")
        y = int(y) - 1
        x = int(x) - 1
        
    A[y][x] = "|*"
    for i in range(n):
        for j in range(n):
            print(A[i][j], end="")
        print("|")
    val = input("Val")


    