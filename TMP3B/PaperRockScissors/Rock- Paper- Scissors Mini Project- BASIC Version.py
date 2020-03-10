movesList = ['rock', 'paper', 'scissors']

validMoves = {
  "paper": True,
  "rock": True,
  "scissors": True
}

# just felt like looping
for move in movesList:
  print(f'...{move}...')

player1 = input("Player 1's choice: ").lower()
player2 = input("Player 2's choice: ").lower()

# impromtu validation
if not player1 in validMoves:
  player1 = False

if not player2 in validMoves:
  player2 = False

print("SHOOT!")

def result(win_res, los_res, winner):
  win_res = win_res.lower().capitalize()
  los_res = los_res.lower()
  print(f'{win_res} beats {los_res}. {winner} wins!')


if player1 and player2:
  if player1 == player2:
    print("It's a tie!")
  elif player1 == "rock" and player2 == "scissors":
    result(player1, player2, "Player 1")
  elif player1 == "paper" and player2 == "rock":
    result(player1, player2, "Player 1")
  elif player1 == "scissors" and player2 == "paper":
    result(player1, player2, "Player 1")
  else:
    result(player2, player1, "Player 2")
else: 
  print("Uh oh, something went wrong!")