def pattern12(n):
    """
     1   6  11  16  21 
     26  31  36  41  46 
     51  56  61  66  71
     76  81  86  91  96
    101 106 111 116 121
    """
    k=1
    for row in range(1,n+1):
        for col in range(1,n+1):
            print("{:3d}".format(k),end=" ")
            k=k+5
        print()    
pattern12(int(input("ENTER THE VALUE OF ROWS:=")))