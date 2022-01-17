def pattern10(n):
    """
    1 1 2 1 3 1 
    1 2 2 2 3 2 
    1 3 2 3 3 3 
    1 4 2 4 3 4 
    1 5 2 5 3 5
    """
    for row in range(1,n+1):
        for col in range(1,n-1):
                print("{} {}".format(col,row),end=" ")
        print()
pattern10(int(input("ENTER THE VALUE OF ROWS:=")))            