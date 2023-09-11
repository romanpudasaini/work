import random
def get_choices():
  player_choice =input("enter the choice:")
  options = ["rock","paper","scissors"]
  computer_choice =random.choice(options)
  choices = {"player" : player_choice,"computer" : computer_choice}
  return(choices)


def check_win(player,computer):
  print(f"you chose {player},computer chose {computer}")
  if player == computer:
    return "It's a tie"
  elif player == "rock":
    if computer == "scissors":
      return " rock smash scissors    You win !!!"
    else:
      return " paper covers rock   you lose"
  elif player == "paper":
    if computer == "rock":
      return " paper cover rock    You win !!!"
    else:
       return " scissorss cut paper  you lose"  
  elif player == "scissors":
     if computer == "paper":
      return " scissors cut paper You win !!!"
  else:
      return " rock smash scissors  you lose"   

choices = get_choices()
result = check_win(choices["player"],choices["computer"])
print(result)