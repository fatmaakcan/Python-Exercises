list=["1","2","5a","10b","abc","10","50"]

#Finding the numbers in the list

for x in list:
    try:
        result=int(x)
        print(result)
    except ValueError:
        continue

print("*****"*10)

#ValueError example with the input from the user

while True:
    number=input("number: ")
    if number=="q":
        print("Exiting...")
        break
    
    try:
        result=int(number)
    except ValueError:
        print("Invalid value!")
        continue

print("*****"*10)

#Mini password validation example

turkish_characters="şçğüöıİ"

password=input("password: ")

for i in password:
    if i in turkish_characters:
        raise TypeError("Password cannot include Turkish characters!")
    else:
        pass
print("Valid password :) ")

print("*****"*10)

#Factorial function example

def factorial(x):
    x=int(x)
    
    if x<0:
        raise ValueError("Negative value")
    
    result=1
    
    for i in range(1,x+1):
        result*=i
    return result

for x in [5,10,20,-3,"10a"]:
    try:
        y=factorial(x)
    except ValueError as err:
        print(err)
        continue
    print(y)   
