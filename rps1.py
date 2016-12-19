import random
import time

#setting the initial variables
rock = 1
paper = 2
scissors = 3

names = { rock: "Rock", paper: "Paper", scissors: "Scissors" }
rules = { rock: scissors, scissors: paper, paper:rock }


#setting the initial scores to 0
player_score = 0
computer_score = 0


#outline of the functions that I will use

def start():

    print "lets play a game of rock, paper , scissors"

    while game():
        pass
    scores()



def game():
    player = move()
    computer = random.randint(1, 3)

    result(player, computer)
    return play_again()

def move():

    while True:
        print
        player_input = raw_input("Rock 1\n, paper 2\n and scissors /3\n make a move")
        try:
            player = int(player_input)
            if player in (1,2,3):
                return player
        except ValueError:
            pass
        print "Please enter 1, 2 or 3"



def result():

def play_again():

def scores():

if __name__ = "__main__":
    start()