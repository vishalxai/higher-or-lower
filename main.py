#Higher or lower project
import game_data
import art
import random
# all the random files have been imported and now need to make one by one def
from art import logo,vs
from game_data import data
print (logo)
#Step 2 Format account data for display
def format_account(account):
    """Takes the account data and returns a printable string."""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description} , from {country}"

#step 3 check user guess
def check_answer(guess,a_followers , b_followers):
    """Checks if user is correct and returns true or false."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
#step 4 : Game logic
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b :
        account_b = random.choice(data)
    print(f"compare A :  {format_account(account_a)}")
    print (vs)
    print(f"Against B {format_account(account_b)}")

    guess = input("who has more followers ?Type 'A' or 'B': " ).lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess,a_follower_count,b_follower_count)

    if is_correct:
        score += 1
        print(f"you are right !current score:{score}")
    else:
        game_should_continue = False
        print(f"sorry,that's wrong .final score :{score} ")
