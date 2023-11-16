import random
COLORS = ['RED', 'GREEN', 'BLUE', 'PURPLE', 'BROWN', 'YELLOW']

def input_color(color):
    return color in COLORS

def create_code():
    l = []
    for i in range(4):
        l.append(random.choice(COLORS))
    return l

def black_pins(guess, code):
    p = 0
    for i in range(4):
        if guess[i] == code[i]:
            p += 1
    return p

def score_guess(guess, code):
    b, p = black_pins(guess, code), 0
    for i in COLORS:
        p += min(guess.count(i), code.count(i))
    return (b, p - b)

def input_guess():
    l = []
    print("Enter your guess:")
    for i in ["1st", "2nd", "3rd", "4th"]:
        g = input(f"{i} color:")
        while g not in COLORS:
            print(f"Please input a color from the list {COLORS}")
            g = input(f"{i} color:")
        l.append(g)
    return l

def one_round(code):
    guess = input_guess()
    score = score_guess(guess, code)
    print(f"Score: {score[0]} black {score[1]} white")
    return score[0] == 4

def play_mastermind(code):
    i = 1
    while True:
        print(f"Round {i}")
        if one_round(code):
            print("You win!")
            return