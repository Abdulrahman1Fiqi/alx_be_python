x = int(input("Enter the size of the pattern: "))
y = x
while x!=0:
    for z in range(y):
        print("*", end="")  
    print("\n")
    x-=1