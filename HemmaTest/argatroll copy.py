
def checksurround(y, x, A, n):
    if A[y][x] == "|*":
        print("Är samma")
        return True
    """ for i in range(y-1, y+1):
        for j in range(x-1, x+1):
            if A[i][j] == "|*":
                print("Går inte")
                return True 
    
    return False"""
    if "|*" in A[y]:
        print("samma rad")
        return True
    
    for i in range(n):
        if A[i][x] =="|*":
            print("Samma kolumn")
            return True
        
        if (x-y+i < n):
            if A[i][x-y+i] == "|*":
                print("Diago")
                return True
        if (x+y-i < n):
            if A[i][x+y-i] =="|*":
                print("Diagonal")
                return True
    return False

def print_board(matrix, size):
    for i in range(size):
        for j in range(size):
            print(matrix[i][j], end="")
        print("|")
  
def initiate_matrix(size):
    A = []
    for i in range(size):
        x = []
        for j in range(size):
            x.append("|_")
        A.append(x)
    return A
    
          
"""A = []
n  = 5
for i in range(n):
    x = []
    for j in range(n):
        x.append("|_")
    A.append(x)"""
        
"""for i in range(n):
    
    for j in range(n):
        print(A[i][j], end="")
    print("|")"""
n = 5
A = initiate_matrix(n)
print_board(A,n)
    
val = input("Val")
while val != "ö":
    
    y, x = val.split(" ")
    y = int(y) - 1
    x = int(x) - 1
    while(checksurround(y,x,A,n)):
        val = input("Val")
        y, x = val.split(" ")
        y = int(y) - 1
        x = int(x) - 1
           
    A[y][x] = "|*"
    """for i in range(n):
        for j in range(n):
            print(A[i][j], end="")
        print("|")"""
    print_board(A, n)
    val = input("Val")


    