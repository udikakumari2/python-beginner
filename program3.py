import random
answer = random.randint(0, 999)
for n in range(0, 10):
    guess = int(input("Guess: "))
    if guess < answer:
        print("Too low!")
    elif guess == answer:
        print("Correct, you got " +
str(answer))
        break
    else:
        print("Too high")