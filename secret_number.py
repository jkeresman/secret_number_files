import random

from player import Player

score_file = "score.txt"
leaderboard_file = "leaderboard.txt"

name = input("Enter your name: ")
secret = random.randint(1, 30)
attempts = 0


def input_check():
    while True:
        try:
            guess = int(input("Guess the secret number (between 1 and 30): "))
            break
        except ValueError as err:
            print(err)
            print("Please try again!!")
    return guess


def try_reading_scores():
    players = []
    try:
        with open(score_file, "r") as scores:
            lines = scores.read().splitlines()
            players = create_players(lines)
    except OSError:
        print("Could not open/read file: ", score_file)

    return players


def create_players(player_data):
    player_list = []
    for data in player_data:
        data = data.split(" ")
        player = Player(data[0], int(data[1]))
        player_list.append(player)

    return player_list


def set_leaderboard():
    with open(leaderboard_file, "w") as leaderboard:
        i = 1
        for p in sorted_players:
            leaderboard.write(f"{i}.{p}\n")
            i += 1


def new_score():
    with open(score_file, "a") as score:
        score.write(f"{name} {attempts}\n")


while True:
    user_guess = input_check()
    attempts += 1

    if user_guess == secret:
        print("You've guessed it!!!")
        print("Attempts needed: " + str(attempts))
        new_score()
        break
    elif user_guess > secret:
        print("Your guess is not correct... try something smaller")
    elif user_guess < secret:
        print("Your guess is not correct... try something bigger")

all_players = try_reading_scores()

sorted_players = sorted(all_players, key=Player.get__score)

set_leaderboard()
