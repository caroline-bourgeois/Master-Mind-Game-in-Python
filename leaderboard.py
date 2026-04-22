'''
    leaderboard
'''
import turtle


def user_name(name):
    try:
        with open("leaderboard.txt", mode="a", encoding="utf-8") as user_name:
            user_name.write(name + "\n")
    except FileNotFoundError:
        print("error - could not find file")

def score_keeper(num_of_guess):
    try:
        with open("leaderboard.txt", mode="a", encoding="utf-8") as score:
            score.write(str(num_of_guess) + "\n")
    except FileNotFoundError:
        print("error - could not find file")

def show_leaderboard():
    '''
        this function displays the leaderboard txt.
        note: the error message for except is not working properly
    '''
    try:
        with open("leaderboard.txt", mode="r", encoding="utf-8") as leaderboard:
            return leaderboard.read()
    except FileNotFoundError:
        error = turtle.Turtle()
        screen.addshape("leaderboard_error.gif")
        error = turtle.Turtle()
        error.shape("leaderboard_error.gif")
        error.up()
        error.goto(150, -290)
