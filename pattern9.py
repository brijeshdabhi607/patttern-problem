def pattern9(n):
    """
    1  2  3  4  5 
    2  4  6  8 10
    3  6  9 12 15
    4  8 12 16 20
    5 10 15 20 25
    """
    for row in range(1,n+1):
        for col in range(1,n+1):
            print("{:2d}".format(row*col),end=" ")    
        print()    
pattern9(int(input("ENTER THE VALUE OF ROWS:=")))     
# print(pattern9.__doc__)   