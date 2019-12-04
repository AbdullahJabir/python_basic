# def add(a,b):
#     return a+b
# num1=int(input("Enter First Number : "))
# num2=int(input("Enter Second Number : "))

# print(add(num1,num2))



# def greater(a,b):
#     if a>b:
#         return a
#     else:
#         return b

# num1=int(input("Enter first Number : " ))
# num2=int(input("Enter Second Number :"))

# bigger=greater(num1,num2)

# print(f"{bigger} is greater" )




def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>c and c>a:
        return b
    else:
        return c

print(greatest(10,20,30))