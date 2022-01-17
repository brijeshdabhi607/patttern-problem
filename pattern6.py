def pattern6(n):
    """
    1  2  3  4  5 
     6  7  8  9 10 
    11 12 13 14 15 
    16 17 18 19 20 
    21 22 23 24 25 
    """
    k=1
    for row in range(1,n+1):
        for col in range(1,n+1):
            print("{:2d}".format(k),end=" ")
            k=k+1
        print()
pattern6(int(input("ENTER A VALUE OF ROWS:=")))            