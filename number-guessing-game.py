import random
num= random.randint(1,10)
total_attempts=int(input("How many attempts do you want? "))
attempts=total_attempts
count=0
while attempts>0:
    guess=int(input("Enter a number between 1 and 10: "))
    attempts-=1
    count+=1
    if guess==num:
        print("TRUE!YOU GUESSED THE NUMBER IN", count, "TRIES!YOUR SCORE IS", 100-((100/total_attempts)*(count-1)))
        break
    elif guess>num:
        print("You need to lower your guess.")
    elif guess<num:
        print("You need to raise your guess.")
    if attempts==0:
        print("GAME OVER! THE NUMBER WAS", num)
        print("YOUR SCORE IS 0")
        