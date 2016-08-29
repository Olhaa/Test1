import random
from math import log, ceil
print ('Do you want to try your luck and guess the number?')
print ('Enter the range. Firstly choose the low value: ')
a = int(raw_input())
print ('And now choose the high value: ')
b = int(raw_input())
num = random.randint(a, b)
max_attempts = int(ceil(log(b - a + 2, 2)))
all_attempts = set()
print ("Sooo, let's do it! What do you think?")
while len(all_attempts) < max_attempts:
    guess = int(raw_input())
    all_attempts.add(guess) 
    if guess < num:
        print ('Nope. The number is bigger.')
    elif guess > num:
        print ('Nope. The number is lesser.')
    elif guess == num:
        break
if guess == num:
    print ('Congratulations! Today is your lucky day! Your guess is right!')
if guess != num:
    print ('Sorry. The number was ' + str(num)+ '.' +' Try again later!')