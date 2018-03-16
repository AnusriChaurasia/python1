a=int(input("Enter a number:"))
def fact(a):
    if a==0:
        return 1
    else:
        return a*fact(a-1)
    
for i in range(0,a):
    print(fact(i))
