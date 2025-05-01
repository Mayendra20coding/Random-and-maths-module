import random
playing=True
number=str(random.randint(10,20))
print('i will genarate a number from 0 to 9,and you hvr to guess the number one digit at a time.')
print('The game ends when you get 1 hero')
while playing:
 guess=input('give me your best guess\n')
 if number==guess:
  print('you have won the game')
  print('The number was',number)
  break
 else:
  print('your guess isnt quite right,try again\n')