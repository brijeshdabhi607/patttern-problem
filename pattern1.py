def pattern1():
    """
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
"""
    for row in range(1,6):
        for col in range(1,6):
            print("*",end=" ")
        print()
# print(pattern1.__doc__)
pattern1()