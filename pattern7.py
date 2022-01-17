def pattern7(n):
    """
     1  3  5  7  9 
    11 13 15 17 19 
    21 23 25 27 29 
    31 33 35 37 39 
    41 43 45 47 49 
    """
    k=1
    for row in range(1,n+1):
        for col in range(1,n+1):
            print("{:2d}".format(k),end=" ")
            k=k+2
        print()
pattern7(int(input("ENTER THE VALUE OF ROWS:=")))            