This is my final project for my CS5001 class using Python and Turtle.

First, I wrote the text version of the game. I created a function that generated a secret code given the color options. Then a function that compared the secret code to the user guess and returned the number of cows and bulls. 


Then, I drew out the game setup using turtle. The rectangles were for the different areas of the game, circles for the marbles, colored circles for the options, and bulls/cows (small circles). I also displayed the check, undo, quit button, and leaderboard. Both the draw_circle() and bull_cow_pegs() returned the x,y coordinates and “white”, indicating they are empty. 

I did NOT use an object-oriented approach for the project. All functions that required a click or used information from a click were nested inside handle_click function (which was most of my functions). I used a dictionary to keep track of where the player was in the game. This function took in 3 parameters, the info from the functions draw_circle, colored_circle, and bulls_cows_pegs. I then defined a function named get_click and called it in main using .onscreenclick. The coordinates from get_click were then used in my click_color function. I had to add extra "padding" to the radius so that the click was more user-friendly. Using the Pythagorean theorem for valid clicks, if the click was valid, the empty circle would turn the color and the colored circle would become white. 


Similarly, I used .onclick in main for the check, undo, and quit button. Unlike click_colors, I didn’t have to specify the parameters for a valid click because .onclick only registers clicks from the specific turtle objects. If any of those functions ran, then they called their matching function inside handle_click.


I next created a function named check_colors that ran if click_check ran. In here, I made sure that the user was at the end of the row. Then called compare_code to check the guess with the secret code and returns bulls & cows, which was used in bulls_cows_color. Once the colors are reset, we move to the next row, set the column to 0, and clear the guess. Then we check if there are 4 bulls, indicating that the user won. If they won, then the score is added based on the number of "rounds" or rows it took to win. If the user lost, then “-“ was added as the score. 

If undo_click ran, then revert_color was called, indicating that the color should be deleted. I used .pop() to take out the last color that was added to the guess and saved it as undo_color. I had to get the coordinate of the circle to undo, which is one back from the circle that it's currently on. Then loop through the color options to get the coordinates and colors. If the color was the same as undo_color, that color was put back into the correct spot for the color options.

If the quit_button function ran, then the user_quit function ran to display the quit message. 


In a new file, I created the leaderboard functions. The function created a text file to keep track of the names and scores. I will note that the error message for show_leaderboard was not working properly, as I didn’t know how to use turtle.Screen() without conflicting with play_area.


I ran tests on my compare_code function to make sure bulls & cows were calculated correctly. I tested if the user got 1 bull and 1 cow, all bulls, all cows, and 2 of each. I hard-coded the secret and the guess and then called compare_code to check each of the colors. If the actual output was as expected, the test passed; if not, the test failed. In either scenario, the test printed the expected and the actual. I also hard-coded the expected output. I modeled the test after our in-class code called "test physics,” but used an if statement to catch the pass versus fail. 
