from cgi import print_environ


def pattern3(n):
    """
    1 2 3 4 5 
    1 2 3 4 5 
    1 2 3 4 5 
    1 2 3 4 5 
    1 2 3 4 5 
    """
    for row in range(1,n+1):
        for col in range(1,n+1):
            print(col,end=" ")
        print() 
pattern3(int(input("ENTER A NUMBER OF ROWS:=")))
print(pattern3.__doc__)
