import random
number = random.randint(1, 100)
name = input("What is your name? ")
counter = 1
print("Hello",name,"Lets play a game,")
if number % 2 == 0: 
    print("The number is even")
else:
    print("The number is odd")
while True:
 guess = int(input("\nGuess a number from 1-100 "))
 if guess < number:
    counter = counter + 1
    print("Guess is too low")
 elif guess > number:
    counter = counter + 1
    print("Guess is too high")
 elif guess == number:
    print("Congrats,",name,"you found the number in",counter,"attempts")
    break
 if counter >= 3:
    print("hint:", number - random.randint(1,20) or number + random.randint(1,20), " The number is near this number")