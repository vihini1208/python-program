x=int(input("enter marks: "))
max=x
y=1
while (y < 5):
    if (max<x):
        max=x
    x=int(input("enter marks: "))
    y=y+1
print(max)   
    
