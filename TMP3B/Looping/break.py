# while True:
#   command = input("Type 'exit' to exit: ")
#   if (command.lower() == 'exit'):
#     break

# for x in range(1, 101):
#   print(x)
#   if x == 3:
#     break

times = int(input('How many times do I have to tell you? '))

for time in range(times):
  print("CLEAN UP YOUR ROOM!")
  if time >= 3:
    print("Do you even listen anymore?")
    break