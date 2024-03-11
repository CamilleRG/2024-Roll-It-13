import random


# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if users don't enter yes  / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")


def instruction():
    print('''

   **** Instructions ****

   TO begin, decide on a score goal; (eg: The first one to get a 
   score of 50 wins).

   For each round of the game, you win points by rolling dice.
   The winner of the round is the one who gets 13 (or slightly less).

   If you win the round, then your score will increase by the 
   number of points that you earned. If your first roll of two 
   dice is a double (eg: both dice show a three). then your score 
   will be DOUBLE the number of points.

   If you lose the round, then you don't get any points.

   If you and the computer tie (eg: you both get a score of 11, 
   then you will have 11 points added to your score.

   Your goal is to try to get to the target score before the
   computer.

   Good luck.

    ''')


# generates an integer between 0 and 6
# to stimulate a roll of a die
def roll_die():
    roll_result = random.randint(1, 6)
    return roll_result


# rolls  two dice and returns total and whether we
# had a double roll
def two_rolls(who):
    double_score = "no"

    # roll two dice
    roll_1 = roll_die()
    roll_2 = roll_die()

    # check if we have a double  score opportunity
    if roll_1 == roll_2:
        double_score = "yes"

    # Find the total points (so far)
    first_points = roll_1 + roll_2

    # Show the user the result
    print(f"{who}: {roll_1} & {roll_2} - Total: {first_points}")

    return first_points, double_score


# Checks that users enter an integer
# that is more than 13
def int_check(question):
    while True:
        error = "Please enter an integer that is 13 or more."

        try:
            response = int(input(question ))

            # checks that the number is more than / equal to 13
            if response < 13:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# finds the lowest, highest and average
def get_stats(stats_lists):

    # sort the lists.
    stats_lists.sort()

    # find lowest, highest and average scores...
    lowest_score = stats_lists[0]
    highest_score = stats_lists[-1]
    average_score = sum(stats_lists) / len(stats_lists)

    return [lowest_score, highest_score, average_score]


# main routine goes here

# initiable user score and computer score
user_score = 0
computer_score = 0

num_rounds = 0

# create lists to hold user and computer score
user_scores = []
comp_scores = []
game_history = []

# Program starts here (with a heading)
print()
print("🎲🎲 Roll it 13 🎲🎲")
print()

# Display instructions if user wants to see them.
want_instruction = yes_no("Do you want to read the instructions? ")
if want_instruction == "yes":
    instruction()

# Get Target score (must be an integer more than 13)
print()
target_score = int_check("Enter a target score: ")
print(target_score)



# Loop game until we have a winner
while user_score < target_score and computer_score < target_score:

    # Add one to the number of rounds (for our testing)
    num_rounds += 1
    print(f"💿💿💿 Round {num_rounds} 💿💿💿")

    # Start of a single round

    # initialise 'pass' variables
    user_pass = "no"
    computer_pass = "no"

    # Starting Round...
    print("Press <enter> to begin this round: ")
    input()

    # Get initial dice rolls for user
    user_first = two_rolls("User")
    user_points = user_first[0]
    double_points = user_first[1]

    # Tell the user if they are eligible for double points
    if double_points == "yes":
        print("If you win this round, you gain double points!")

    # Get initial dice rolls for computer
    computer_first = two_rolls("Computer")
    computer_points = computer_first[0]

    # Loop (while both user / computer have <= 13 points)...
    while computer_points <= 13 and user_points <= 13:

        # ask user if they want to roll again, update
        # points / status
        print()

        # If user has 13 points, we acn assume they don't want to roll again!
        if user_points == 13:
            user_pass = "yes"
            
        if user_pass == "no":
            roll_again = yes_no("Do you want to roll the dice (type 'no' to pass): ")
        else:
            roll_again = "no"

        if roll_again == "yes":
            user_move = roll_die()
            user_points += user_move

            # If user goes over 13 points, tell them that they lose and set points to 0
            if user_points > 13:
                print(f"💥💥💥 Oops! You have rolled a {user_move} so your total is {user_points}. "
                      f"Which is over 13 points.💥💥💥")

                # reset user points to zero so that when we update their
                # score at the end of round it is correct.
                user_points = 0

                break

            else:
                print(f"You rolled a {user_move} and have a total score of {user_points}.")

        else:
            # if user passes, we don't want to let them roll again!
            user_pass = "yes"

        # if computer has 10 points or more (and is winning), it should pass!
        if computer_points >= 10 and computer_points >= user_points:
            computer_pass = "yes"

        # Don't let the computer roll again if the pass condition
        # has been met in a previous iteration through the loop.
        elif computer_pass == "yes":
            pass

        else:
            # Roll dice for computer and update computer points
            computer_move = roll_die()
            computer_points += computer_move

            # check computer has not gone over...
            if computer_points > 13:
                print(f"💥💥💥The computer rolled a {computer_move}, taking their points"
                      f" to {computer_points}. This is over 13 points so the computer loses!💥💥💥")
                computer_points = 0
                break

            else:
                print(f"The computer rolled a {computer_move}.  The computer"
                      f" now has {computer_points}.")

        print()
        # Tell user if they are winning, losing or if it's a tie.
        if user_points > computer_points:
            result = "🙂🙂🙂 You are ahead. 🙂🙂🙂"
        elif user_points < computer_points:
            result = "😦😦😦The computer is ahead! 😦😦😦"
        else:
            result = "👀It's currently a tie.👀"

        print(f"{result} \tUser: {user_points} \t | \t Computer: {computer_points}")

        if computer_pass == "yes" and user_pass == "yes":
            break

    # Outside loop - double user points if they won and are eligible

    # Show rounds result
    if user_points < computer_points:
        print()
        print("😢😢😢 Sorry - you lost this round and no points "
              f"have been added to your total score. The computer's score has "
              f"increased by {computer_points} points.😢😢😢")

        add_points = computer_points

    # currently does not include double points!
    elif user_points > computer_points:
        # Double user points if they are eligible
        if double_points == "yes":
            user_points *= 2

        print()
        print(f"👍👍👍 Yay! You won the round and {user_points} points have "
              f"been added to you score 👍👍👍")

        add_points = user_points

    else:
        print()
        print(f"👔👔👔 The result for this round is a tie. You and the computer "
              f" both have {user_points}.👔👔👔")

        add_points = user_points

    # Record rounds result and add it to the game history
    round_result = f"Round {num_rounds} - User:  {user_points} \t Computer: {computer_points}"
    game_history.append(round_result)

    # end of a single round

    # if the computer wins, add its points to its score
    if user_points < computer_points:
        computer_score += add_points

    # If the user wins, add its points to its score
    elif user_points < computer_points:
        user_score += add_points

    # if it's a tie, add the poitns to BOTH SCORES
    else:
        computer_score += add_points
        user_score += add_points

    user_scores.append(user_points)
    comp_scores.append(computer_points)

    print()
    print(f"🎲🎲🎲 User: {user_score} points | Computer: {computer_score} points 🎲🎲🎲 ")
    print()

print()

# Display final winner and score information.
print()
if user_score > computer_score:
    print("👍👍👍 Game Over - You Won 👍👍👍")
elif user_score < computer_score:
    print("👎👎👎 Game Over - You lost 👎👎👎")
else:
    print("👔👔👔 Game Over - It's a Tie 👔👔👔")

print(f"Final Scores: User ({user_score}) vs Computer ({computer_score})")
print()

# Display game history if user wants to see it
show_history = yes_no("Do you want to see the game history?")
if show_history == "yes":
    print("\n⌛⌛⌛Game History⌛⌛⌛")

    for item in game_history:
        print(item)

    print()

# calculate the lowest, highest and average
# scores and display them.

user_stats = get_stats(user_scores)
comp_stats = get_stats(comp_scores)

print("📊📊📊 Game Statistics 📊📊📊 ")
print(f"User     - Lowest Score: {user_stats[0]}\t "
      f"Highest Score: {user_stats[1]}\t "
      f"Average Score: {user_stats[2]:.2f}")

print(f"Computer - Lowest Score: {comp_stats[0]}\t "
      f"Highest Score: {comp_stats[1]}\t "
      f"Average Score: {comp_stats[2]:.2f}")

print()
print("Thank you for playing.")