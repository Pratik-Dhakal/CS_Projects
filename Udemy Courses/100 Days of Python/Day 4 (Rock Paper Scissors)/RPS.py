import random 
rock = ''' #Picture for the Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = ''' #Picture for the Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = ''' #Picture for the Scissors
    _______
---'   ____)____
          ______) 
       __________)
      (____)
---.__(___)
'''

play = int(input("What do you choose, type 0 for rock, 1 for paper, and 2 for scissors and 3 to quit\n"))  # This gets the input from the user

while play != 3: #This makes sures that the loop goes on until the user enters 3

  if play == 0: # The code here prints out whatever the user enters
    print(rock)
  if play == 1:
    print(paper)
  if play == 2:
    print(scissors)


  print("The computer chose: \n")

  random_num = random.randint(0,2) #This code generates a random number for the computer's choice and prints a picture based on that

  if random_num == 0:
    print(rock)
  if random_num == 1:
    print(paper)
  if random_num == 2:
    print(scissors)

  if play == random_num: #These are all the different combinations for wins and loses
    print("It's a draw")
  elif play == 0 and random_num == 1: #user -> rock  | computer -> paper
    print("You lose")
  elif play == 1 and random_num == 0: #user -> paper  | computer -> rock
    print("You win")
  elif play == 0 and random_num == 2: #user -> rock  | computer -> scissors
    print("You win")
  elif play == 2 and random_num == 0: #user -> scissors  | computer -> rock
    print("You lose")
  elif play == 1 and random_num == 2: #user -> paper  | computer -> scissors
    print("You lose")
  elif play == 2 and random_num == 1: #user -> scissors  | computer -> paper
    print("You win")
  
  print("\n\n")
  
  play = int(input("What do you choose, type 0 for rock, 1 for paper, and 2 for scissors and 3 to quit\n")) #This gets the input for reprompting

print("Thank you for playing ") #If the use enters 3, this is what they see
