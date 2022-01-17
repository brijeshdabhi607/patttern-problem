def pattern4(n):
    """
    5 4 3 2 1 
    5 4 3 2 1 
    5 4 3 2 1
    5 4 3 2 1
    5 4 3 2 1
    """
    for row in range(n,0,-1):
        for col in range(n,0,-1):
            print(col,end=" ")
        print()
pattern4(int(input("ENTER A NUMBER OF ROWS:=")))            