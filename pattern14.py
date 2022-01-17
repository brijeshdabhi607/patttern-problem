def pattern14(n):
    for row in range(1,n+1):
        p=n-row+1
        for col in range(1,n+1):
            print("{:2d}".format(p),end=" ")
            p=p+n
        print()
pattern14(int(input("ENTER THE VALUE OF ROWS:=")))