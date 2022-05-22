
import random
print("Number guessingGame")
number = random.randint(1, 9)
chances=0
print("Guess a number (between 1 and 9)")

while chances < 5:
  guess = int(input("Enter your guess:"))
  chances+=1   
  if guess == number:
    print("Congratulations You won!!!")
    break
  elif guess < number:
    print("Your guess was too low!Try the number higher than",guess)
  else:
    print("Your guess was too hight!Try the number lower than",guess)


if not chances < 5:
  print("You Lose!!!The number is",number)

    

