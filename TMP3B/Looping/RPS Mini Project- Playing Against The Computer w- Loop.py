from random import choice 

movesList = ['rock', 'paper', 'scissors']

validMoves = {
  "paper": True,
  "rock": True,
  "scissors": True
}

initializing = True

while (initializing):
  player_wins = 0
  computer_wins = 0
  winning_score = input('How many wins do you want to play up to? ')
  if winning_score == 'quit' or winning_score == 'q':
    break
  winning_score = int(winning_score)

  while player_wins < winning_score and computer_wins < winning_score:

    print(f'Player Score: {player_wins} Computer Score: {computer_wins}')
    # just felt like looping
    for move in movesList:
      print(f'...{move}...')

    player = input("Player, make your choice: ").lower()
    if player == 'quit' or player == 'q':
      break
    # not sure why randomint was recommended when choice removes a lot of steps.
    computer = choice(movesList)

    # impromtu validation
    if not player in validMoves:
      player = False

    if not computer in validMoves:
      computer = False

    print(f"Computer players {computer}.")

    # Result after ever turn

    def result(win_res, los_res, winner):
      win_res = win_res.lower().capitalize()
      los_res = los_res.lower()
      print(f'{win_res} beats {los_res}. {winner.capitalize()} earns 1 point!')
    
    # Scoring Logic
    if player and computer:
      if player == computer:
        print("It's a tie!")
      elif player == "rock" and computer == "scissors":
        result(player, computer, "player")
        player_wins += 1 
      elif player == "paper" and computer == "rock":
        result(player, computer, "player")
        player_wins += 1
      elif player == "scissors" and computer == "paper":
        result(player, computer, "player")
        player_wins += 1 
      else:
        result(computer, player, "computer")
        computer_wins += 1
    else: 
      print("Uh oh, something went wrong!")

  if player_wins > computer_wins:
    print('Congratulations! You Win!')
  elif player_wins == computer_wins:
    print('It\'s a tie!')
  else:
    print('Sorry! You lose! Computer Wins!')
  print(f'Final Scores -- Player: {player_wins}. Computer {computer_wins}.')


  # Do you want to play again?

  play_again = input('Do you want to play again? (y/n) ').lower()
  if play_again == 'n':
    initializing = False
  elif player_again == 'y':
    initializing = True
  else:
    play_again = input('Sorry, I didn\'t get that. Did you want to play again? (y/n) ')

# Exiting Message

if initializing == True:
  print('Hate to see you go! Wish we could\'ve played!')
else: 
  print('Thanks for playing! See you again!')