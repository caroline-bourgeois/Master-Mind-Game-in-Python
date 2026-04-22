
import random

def get_secret_code():
    ''' this function gets the secret code for the game '''

    # color options for secret code
    colors = ["red", "blue", "green", "yellow", "purple", "black"]
    # list to store secret code
    secret_code = []

    # run loop 4 times (iteration num doesnt matter)
    for _ in range(4):
        # pick random index 
        index = random.randint(0, len(colors) -1 )
        # pop from color so that it cant be picked twice & add color to secret code
        secret_code.append(colors.pop(index))

    return secret_code

def compare_code(secret_code, guess):
    ''' this compares secret code to guess and returns cows and bulls '''
    
    bulls = 0   # correct color & position
    cows = 0    # color color. wrong position

    for i in range(len(secret_code)):
        if guess[i] == secret_code[i]:
            bulls += 1
    
    for i in range(len(guess)):
        if guess[i] in secret_code and guess[i] != secret_code[i]:
            cows += 1

    return (bulls, cows)

def main():
    pass
if __name__ == "__main__":
    main()
