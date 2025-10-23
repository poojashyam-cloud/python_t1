import random
print("Hi! Welcome to the Number Guessing Game. \nYou have 5 chances to Guess the number. \nLet's start the game")
lb = int(input("Enter Lower boundary number: "))
ub = int(input("Enter Upper boundary number: "))
print(f"\nYou have 5 chances to guess the number between {lb} and {ub} .\nLet's Start !")
num = random.randint(lb,ub)
ch=5 #total chances allowed to guess
gc=0 #guess count
while gc < ch:
    gc += 1
    guess = int(input("\nEnter your guess : "))
    if guess == num:
        print (f"Correct !! the number is {num} ,you guessed it in {gc} attempt.")
        break
    elif gc >= ch and guess != num:
        print(f"Sorry ! the number is {num} .\nBetter Luck ! next time.")
    elif guess > num:
        print("Too High ! Try lower number ")
    elif guess < num:
        print("Too Low ! Try higher number ")


