import random
choices = ['rock', 'paper', 'scissors']
user= input("Choose rock, paper, or scissors: ").lower()
computer= random.choice(choices)
print(f"\nYou chose: {user}")
print(f"Computer chose: {computer}")
if user== computer:
    print("It's a tie!")
elif (user== 'rock' and computer== 'scissors'):
     print("You win!")
elif(user== 'scissors' and computer== 'paper'):
     print("You win!")
elif(user== 'paper' and computer== 'rock'):
     print("You win!")
else:
    print("You lose!")
