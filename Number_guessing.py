import random

print("Welcome to Python Number Guessing game !\n")

n=int(input("Enter the number upto computer select a number : "))
num=random.randint(1,n)

attempt=0
while True:
    attempt+=1

    user=int(input("Enter the number by guess : "))

    if user>num:
        print("Your number is too high! Try again.")

    elif user<num:
        print("Your number is too low! Try again.")

    elif user==num:
        print(f"Congratulations! You guessed the number {num} in {attempt} attempts.")
        break
