'''import random
guess=(1,2,3)
rando=(random.choice(guess))

for i in range(0,3):
    a = input("number? ")
    if (a != rando):
        print ("try again")
    else:
        print ("congrats")
    quit()'''

import random
n = random.randint(1, 10)
guess = int(input("Enter an integer from 1 to 10: "))
range = 0
while n != "guess" and range !=3:
    print
    if guess < n:
        print ("guess is low")
        guess = int(input("Enter an integer from 1 to 10: "))
    elif guess > n:
        print ("guess is high")
        guess = int(input("Enter an integer from 1 to 10: "))
    else:

        print ("you guessed it!")
        break
    print

'''import random
n = random.randint(1, 10)
print (n)
#guess = int(input("number?"))
for a in range(0,3):
    guess = int(input("number?"))
    if guess == n:

        print("congrats")
    else:
        print("try again")'''

