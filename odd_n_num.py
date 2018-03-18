"""def my_sol():
    numbers=[input("enter a value:") for i in range(10)]
    odds=[y for y in numbers if y%2!=0]
    if odds:
        return max(odds)
    else:
        return "all declared nums are even."
    
my_sol()"""

maxOdd=None
for i in range(5):
    value=int(input("Enter a value: "))
    if(value % 2 and(maxOdd is None or value > maxOdd)):
        maxOdd = value
if maxOdd:
    print("largest odd num is ",maxOdd)
else:
    print("No odd values")
print(type(maxOdd))    
