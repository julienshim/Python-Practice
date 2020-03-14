from random import choice 

movesList = ['rock', 'paper', 'scissors']

validMoves = {
  "paper": True,
  "rock": True,
  "scissors": True
}

# just felt like looping
for move in movesList:
  print(f'...{move}...')

player = input("Player, make your choice: ").lower()
# not sure why randomint was recommended when choice removes a lot of steps.
computer = choice(movesList)

# impromtu validation
if not player in validMoves:
  player = False

if not computer in validMoves:
  computer = False

print(f"Computer players {computer}.")

def result(win_res, los_res, winner):
  win_res = win_res.lower().capitalize()
  los_res = los_res.lower()
  print(f'{win_res} beats {los_res}. {winner} wins!')
  if (winner == 'player') {
    player_wins
  }


if player and computer:
  if player == computer:
    print("It's a tie!")
  elif player == "rock" and computer == "scissors":
    result(player, computer, "Player")
  elif player == "paper" and computer == "rock":
    result(player, computer, "Player")
  elif player == "scissors" and computer == "paper":
    result(player, computer, "Player")
  else:
    result(computer, player, "Computer")
else: 
  print("Uh oh, something went wrong!")
