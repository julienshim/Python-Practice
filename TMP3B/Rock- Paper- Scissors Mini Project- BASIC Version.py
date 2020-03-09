movesList = ['rock', 'paper', 'scissors']

validMoves = {
  "paper": True,
  "rock": True,
  "scissors": True
}

# just felt like looping
for move in movesList:
  print(f'...{move}...')

player1 = input("Player 1's choice: ")
player2 = input("Player 2's choice: ")

# impromtu validation
if not player1 in validMoves:
  player1 = False

if not player2 in validMoves:
  player2 = False

print("SHOOT!")

if player1 and player2:
  if player1 == player2:
    print("It's a tie!")
  elif player1 == "rock":
    if player2 == "scissors":
        print("Rock beats scissors. Player 1 wins!")
    elif player == "paper":
        print("Paper beats rock. Player 2 wins!")
  elif player1 == "paper":
    if player2 == "rock":
      print("Paper beats rock. Player 1 wins!")
    elif player == "scissors":
      print("Scissors beats paper. Player 2 wins!")
  elif player2 == "scissors":
    if player2 == "paper":
      print("Scissors beats paper. Player 1 wins!")
  elif player == "rock":
      print("Paper beats rock. Player 2 wins!")
else: 
  print("Uh oh, something went wrong!")