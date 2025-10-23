import random
print("Hi!! Welcom to Word Scramble game.\nGuess the correct word ")
words = ['python','javascript','java','automation','pytest','guvi','selenium']
while True:
    word = random.choice(words)
    jumbled_word = list(word)
    random.shuffle(jumbled_word)
    jumbled_word = ''.join(jumbled_word)
    print("Jumbled input : ",jumbled_word)

    guess = input("player guess : ")
    if guess == word :
        print("Correct!!")
    else:
        print("Incorrect!!")

    play_again = input("want to play again ? (yes/no): ")
    if play_again.lower() != "yes":
        print("game ends")
        break