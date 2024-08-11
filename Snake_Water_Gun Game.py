import random
print("Welcome to Snake Water gun game You have to play 10 times to get winner  !!")
score_user = 0
score_comp = 0
i = 1
def get_compchoice():
    ch = ["Snake", "Water", "Gun"]
    return random.choice(ch)
def get_winner(u_score, c_score):
    if u_score > c_score:
        print(f"You Win !! Your Score: {u_score}, Computer Score: {c_score}")
    elif u_score < c_score:
        print(f"You Lose !! Your Score: {u_score}, Computer Score: {c_score}")
    elif u_score==c_score==0:
        print("Thanks for Playing !!!")
    else:
        print(f"Score is Tie. Your Score: {u_score}, Computer Score: {c_score}")
while i <= 4:
    ch = ["Snake", "Water", "Gun"]
    user_choice = input("Enter your Choice: Snake, Water or Gun or Quite to exit \n").capitalize()
    if user_choice == "Quite":
        break
    if user_choice not in ch:
        print("Please Enter valid input")
        continue

    comp_choice = get_compchoice()
    print(f"Computer chose: {comp_choice}")

    if user_choice == comp_choice:
        print("Score is Tie for this round")
    elif (user_choice == "Gun" and comp_choice == "Snake") or \
            (user_choice == "Water" and comp_choice == "Gun") or \
            (user_choice == "Snake" and comp_choice == "Water"):
        print("You win this round!")
        score_user += 5
    else:
        print("Computer wins this round!")
        score_comp += 5
    i += 1
get_winner(score_user, score_comp)
