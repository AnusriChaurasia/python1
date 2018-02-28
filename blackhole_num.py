dict_a={1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}
a=input("Enter a word.")
while(True):
    b=len(a)
    a=dict_a[b]
    print(a)
    if(len(a)==4):
        print(dict_a[len(a)])
        break
    
    
