# Faulti Calculator it gives the false calculation for [45*6 =555, 56+7=77, 56/8=9] Otherwise give the correct 
a= int(input("Enter your 1st number "))

print( "Select the operator \n Enter + for addition \n Enter - for substraction \n Enter * for multiplication \n Enter / for division ")
op= input()
b= int(input("Enter your 2nd number "))
if op=="+" :
    if a==56 and b==7:
        print("Sum of number is 77")
    else:
        print("Sum of number is ", a+b)
elif op=="-" :
    print("Substraction of number is ",a -b)
elif op=="*" :
    if a==45 and b==6:
        print("Multiplication of number is 555")
    else:
        print("Multiplication of number is ",a *b)
elif op=="/" :
    if a==56 and b==8:
        print("Divison of number is 9")
    else:
        print("Division of number is ",a /b)
else:
    print("Please Enter a valid operator")