weight=int(input("enter weight"))
height=int(input("enter height"))
BMI=weight/height**2
if BMI >=30:
   print("obese")
elif BMI >=25:
   print("over weight")
elif BMI >=18:
    print("normal weight")
else :
    print("under weight")
