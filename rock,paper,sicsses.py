import random
while True:
 user_action=input('Enter your choice(rock,paper,scissors):')
 possible_actions=['rock','paper','scissors']
 computer_action=random.choice(possible_actions)
 print(f'you chose{user_action},computer chose{computer_action}')
 if user_action==computer_action:
  print(f'both player selected {user_action}.its a tie ')
 elif user_action=='rock':
  if computer_action=='scissors':
   print('rock smashers scissors. You win')
  else:
   print('paper covers rock. You lose')
 elif user_action=='paper':
  if computer_action=='rock':
   print('paper cover rock. You win')
  else:
   print('scissors cut paper. You lose')
 elif user_action=='scissors':
  if computer_action=='paper':
   print('scissors cut paper. You win')
  else:
   print('rock smashes scissors. You lose')
 play_again=input('play again?(y/n)')
 if play_again !='y':
  break