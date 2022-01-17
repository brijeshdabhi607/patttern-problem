def pattern8(n):
    """
     2  4  6  8 10 
    12 14 16 18 20 
    22 24 26 28 30 
    32 34 36 38 40 
    42 44 46 48 50 
    """
    k=2
    for row in range(1,n+1):
        for col in range(1,n+1):
            print("{:2d}".format(k),end=" ")
            k=k+2
        print()    
pattern8(int(input("ENTER THE VALUE OF ROWS:=")))    