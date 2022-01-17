def pattern11(n):
    """
    1 1 1 2 1 3 
    2 1 2 2 2 3 
    3 1 3 2 3 3 
    4 1 4 2 4 3 
    5 1 5 2 5 3 
    """
    for row in range(1,n+1):
        for col in range(1,n-1):
            print("{} {}".format(row,col),end=" ")
        print()
pattern11(int(input("ENTER THE NUMBER OF ROWS:=")))            