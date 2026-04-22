'''
    Caroline Bourgeois
    Spring 2026
    Final Project
    Mastermind Game
'''

import turtle
from get_color import *
from leaderboard import *

# screen & circle dimensions
WIDTH = 1000
HEIGHT = 1000
RADIUS = 20
SMALL_CIRCLE = 8

# setup screen
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
pen = turtle.Turtle()

# circle x,y & space setup
circle_x = -400
circle_y = 350
spacing = 55

def draw_play_area():
    '''
        this function draws the play area of the game
    '''

    pen.speed(0)
    pen.up()
    pen.goto(-480, 390)
    pen.down()
    pen.forward(700)
    pen.right(90)
    pen.forward(620)
    pen.right(90)
    pen.forward(700)
    pen.right(90)
    pen.forward(620)
    pen.up()

def draw_score_area():
    '''
        this function draws the score area of the game
    '''
    pen.speed(0)
    pen.up()
    pen.goto(250, 390)
    pen.down()
    pen.right(90)
    pen.forward(200)
    pen.right(90)
    pen.forward(620)
    pen.right(90)
    pen.forward(200)
    pen.right(90)
    pen.forward(620)
    pen.up()

def draw_status_area():
    '''
        this function draws the color status area of the game
    '''

    pen.speed(0)
    pen.up()
    pen.goto(445, -250)
    pen.color("lightgrey")
    pen.begin_fill()
    pen.down()
    pen.left(90)
    pen.forward(920)
    pen.left(90)
    pen.forward(100)
    pen.left(90)
    pen.forward(920)
    pen.left(90)
    pen.forward(100)
    pen.end_fill()

def draw_circle():
    '''
        this function draws the circles for the game
    '''

    # empty list to collect all circle position
    circle_position = []

    for row in range(10):

        # empty list to collect circle rows
        row_position = []

        for col in range(4):
            x = circle_x + col * spacing
            y = circle_y - row * 60
            pen.up()
            pen.goto(x,y - RADIUS)
            pen.setheading(0)
            pen.down()
            pen.pencolor("black")
            pen.circle(RADIUS)

            row_position.append((x, y, "white"))
        circle_position.append(row_position)
    return circle_position

def colored_circle():
    '''
        this function draws the colored circles for the game
    '''

    color_options = ["red", "blue", "green", "yellow", "purple", "black"]

    # empty list to store the circle positions
    corlor_circle_pos = []
    
    for i in range(6):
        pen.up()
        x = circle_x + i * spacing
        y = -280
        color = color_options[i]
        pen.goto(x,y - RADIUS)
        pen.setheading(0)
        pen.down()
        pen.fillcolor(color)
        pen.begin_fill()
        pen.circle(RADIUS)
        pen.end_fill()

        corlor_circle_pos.append((x,y, color))
    return corlor_circle_pos

def bull_cow_pegs():
    '''
        this function draws the bulls & cows for the game
    '''

    # empty list to collect the positions
    bull_cow_position = []

    for i in range(10):
        row_position = []

        # row that matches row in big circles
        y_base = circle_y - i * 60 + 5

        # x_coord, y_coord relative to big circles
        coords = [(0,0), (22, 0), (0, -22), (22, -22)]

        for x_coord, y_coord in coords:
            x = 30 + x_coord
            y = y_base + y_coord

            pen.up()
            pen.goto(x, y - SMALL_CIRCLE)
            pen.down()
            pen.circle(SMALL_CIRCLE)

            row_position.append((x, y, "white"))
        bull_cow_position.append(row_position)
    return bull_cow_position

def draw_check_button():
    '''
        this function draws the check mark button
    '''

    screen.addshape("checkbutton.gif")
    check_mark = turtle.Turtle()
    check_mark.shape("checkbutton.gif")
    check_mark.up()
    check_mark.goto(40, -290)
    return check_mark

def draw_undo_button():
    '''
        this function draws the x/undo button
    '''

    screen.addshape("xbutton.gif")
    undo_mark = turtle.Turtle()
    undo_mark.shape("xbutton.gif")
    undo_mark.up()
    undo_mark.goto(150, -290)
    return undo_mark

def draw_quit_button():
    '''
        this function draws the quit button
    '''

    screen.addshape("quit.gif")
    quit_button = turtle.Turtle()
    quit_button.shape("quit.gif")
    quit_button.up()
    quit_button.goto(350, -290)
    return quit_button

def display_leaderboard():
    '''
        this function shows the leaderboard from show leaderboard function and writes on the screen
    '''

    scores = show_leaderboard()
    pen.up()
    pen.goto(270, 300)
    pen.color("black")
    pen.write(scores, font=("Arial", 16, "bold"))

def you_win():
    '''
        this function shows the win gif
    '''

    screen.addshape("winner.gif")
    winner = turtle.Turtle()
    winner.shape("winner.gif")
    winner.up()
    winner.goto(30, 200)
    return winner

def you_lose():
    ''' this function shows the lose gif '''

    screen.addshape("lose.gif")
    lose = turtle.Turtle()
    lose.shape("lose.gif")
    lose.up()
    lose.goto(30, 200)
    return lose

def handle_click(circle_location, color_options, bull_cow_circle):
    ''' this function handles all the clicks in the game '''

    # dictionary to track where player is in game
    current_play = {"current_row": 0, "current_col": 0, "current_guess": [], "code": get_secret_code()}

    def click_color(click_x, click_y):
        ''' this function makes colored circle white and empty circle the color that was clicked '''

    # if click not in colored circle
        if abs(click_y - color_options[0][1]) > RADIUS + 10:
            return None, None
        
        # get the x & y for each of the colored circles
        for color_i in range(len(color_options)):
            x, y, colors = color_options[color_i]

            # x & y for valid clicks
            use_x = click_x - x
            use_y = click_y - y

            # if click w/in color circle -> make white
            if use_x*use_x + use_y*use_y <= (RADIUS + 10) **2:

                pen.up()
                pen.goto(x, y - RADIUS)
                pen.setheading(0)
                pen.fillcolor("white")
                pen.begin_fill()
                pen.down()
                pen.circle(RADIUS)
                pen.end_fill()

                # get the position of row user is at
                get_row = circle_location[current_play["current_row"]]

                # get the x & y coords, forget about the color (_)
                fill_x, fill_y, _ = get_row[current_play["current_col"]]

                pen.up()
                pen.goto(fill_x, fill_y - RADIUS)
                pen.setheading(0)
                pen.fillcolor(colors)
                pen.begin_fill()
                pen.down()
                pen.circle(RADIUS)
                pen.end_fill()

                # add the color to the guess and move to next circle 
                current_play["current_guess"].append(colors)
                current_play["current_col"]+= 1

                return color_i, colors
        return None, None
    
    def bull_cow_color(bulls, cows):
        ''' this function colors in the bulls & cows '''

        b_and_c = bulls + cows
        b_c_row = current_play["current_row"]

        print(f" {bulls} + {cows} = {b_and_c}")
        
        # loop through bulls & cows to know how many to fill
        for i in range(b_and_c):

            # get x,y coords 
            bull_cow_x, bull_cow_y, _ = bull_cow_circle[b_c_row][i]

            if i < bulls:
                pen.fillcolor("black")
            else:
                pen.fillcolor("red")

            pen.up()
            pen.goto(bull_cow_x, bull_cow_y - SMALL_CIRCLE)
            pen.setheading(0)
            pen.down()
            pen.begin_fill()
            pen.circle(SMALL_CIRCLE)
            pen.end_fill()
    
    def get_click(x, y):
        ''' this function gets the click for click color'''

        # gets click coordinates for click color
        click_color(x,y)

    def click_check(x, y):
        ''' this function gets the click for check mark '''
        
        # user clicks check -> go to check_colors
        check_colors()

    def check_colors():
        ''' 
            check colors after user clicks check
            it compares code with current_guess, calls bull_cow_color, 
            reset the colors, moves to the next round, and checks the score.
        '''

        # make sure all the circles are colored
        if current_play["current_col"] == 4:

            # use code & current guess in compare code -> save return as bulls, cows
            bull, cows = compare_code(current_play["code"], current_play["current_guess"])

            print(current_play["code"])
            print(current_play["current_guess"])

            # use num of bulls & cows in bull_cow_color
            bull_cow_color(bull, cows)

            # reset the color options
            colored_circle()

            # move to next row, set the column back to 0, set the guess back to empty
            current_play["current_row"] += 1
            current_play["current_col"] = 0
            current_play["current_guess"] = []

            # if 4 bulls, write the score as num of guesses it took, display you win gif
            if bull == 4:
                score_keeper(current_play["current_row"])
                you_win()

            # if at the end of row, display lose gif
            elif current_play["current_row"] == 10:
                score_keeper("-")
                you_lose()
        else:
            return None
    
    def undo_click(x,y):
        ''' gets the click for undo button and calls revert colors '''
        
        # when undo button clicked call revert_color
        revert_color()
        
    def revert_color():
        ''' 
            this reverts the color back into the options, takes off the last guess,
            goes back 1 on the column to make the circle white, 
            puts color back into the options
        '''

        # make sure at least one color has been added to be able to undo
        if current_play["current_col"] > 0:

            # take out last color added to current guess
            undo_color = current_play["current_guess"].pop()

            # find row of circle to undo
            undo_row = circle_location[current_play["current_row"]]

            # get the x,y, nothing(_) from the row & column -1
            undo_x, undo_y, _ = undo_row[current_play["current_col"]-1]
            
            pen.up()
            pen.goto(undo_x, undo_y - RADIUS)
            pen.setheading(0)
            pen.fillcolor("white")
            pen.begin_fill()
            pen.down()
            pen.circle(RADIUS)
            pen.end_fill()

            # get the x,y, colors from color_options
            for color_i in range(len(color_options)):
                x, y, colors = color_options[color_i]

                # check if color matches undo color -> put color back in circle
                if colors == undo_color:
                    pen.up()
                    pen.goto(x, y - RADIUS)
                    pen.setheading(0)
                    pen.fillcolor(colors)
                    pen.begin_fill()
                    pen.down()
                    pen.circle(RADIUS)
                    pen.end_fill()

            # because undo circle, column is one back
            current_play["current_col"] -= 1
    
    def user_quit(x, y):
        ''' this function displays the quit message if the quit button is clicked '''

        screen.addshape("quitmsg.gif")
        quit_message = turtle.Turtle()
        quit_message.shape("quitmsg.gif")
        quit_message.up()
        quit_message.goto(30, 200)

    return get_click, click_check, undo_click, user_quit

def main():
    # play area of game
    draw_play_area()
    draw_score_area()
    draw_status_area()

    # circles for game
    circle_location = draw_circle()
    color_options = colored_circle()
    bull_cow_circle = bull_cow_pegs()

    # buttons for game
    check_mark = draw_check_button()
    undo_mark = draw_undo_button()
    quit_button = draw_quit_button()

    # welcome message for leaderboard
    name = screen.textinput("welcome to mastermind", "enter your name: ")
    # add name to leaderboard
    user_name(name)

    # save the returns from handle_click to use below
    get_click, click_check, undo_click, user_quit = handle_click(circle_location, color_options, bull_cow_circle)
    
    # when button is clicked, call functions
    check_mark.onclick(click_check)
    undo_mark.onclick(undo_click)
    quit_button.onclick(user_quit)
    screen.onscreenclick(get_click)

    # show leaderboard
    display_leaderboard()

    # print("registering click handler")
    turtle.done()

if __name__ == "__main__":
    main()
