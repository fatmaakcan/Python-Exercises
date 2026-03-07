def displayWord (word, times):
    print(word * times)

displayWord("Hello ", 5)

print("*********" * 10)

def add (*args):
    return list(args)

print(add(1, 2, 3, 4, 5,"Merhaba")) 

print("*********" * 10)

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

def primeNum(num1,num2):
    print(f"Prime numbers from {num1} to {num2} are:")
    for num in range(num1,num2+1):
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                print(num)
primeNum(num1,num2)

print("*********" * 10) 

def findDivider(num):
    for i in range(1,num+1):
        if num%i==0:
            print(i)
num=int(input("Enter a number:"))
print(num,"'s dividers are:")
findDivider(num)
