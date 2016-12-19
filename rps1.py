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