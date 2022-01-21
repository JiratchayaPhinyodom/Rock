
p = int(input("Enter number of players: "))
r = int(input("Enter number of rounds: "))
#Create Function
def initialize_list(p):
    list1 = []
    for i in range(p):
        list1.append(0) #In initializing append distance of players = 0.
    return list1

def print_two_team_stat(list1,list2):
    print(f"Team 1 : {str(list1)}")
    print(f"Team 2 : {str(list2)}")

import random
def randomize_player(p):
    return random.randint(1,p) #Randomize an integer between 1 and p

def randomize_hand(): #Randomize integer between 1 and 3
    for i in range(p):
        if randomize_player(p) == 1:
            return "Rock"
        elif randomize_player(p) == 2:
            return "Paper"
        else:
            return "Scissors"

def play_one_round(list1,list2): #Random choose one player from each team to play
        one = randomize_hand()
        two = randomize_hand()
        player1 = randomize_player(len(list1))
        player2 = randomize_player(len(list2))
        print(f"Team 1: Player {player1} plays with Hand: {one}")
        print(f"Team 1: Player {player2} plays with Hand: {two}")
        find_winner = find_round_winner(one, two)
        report_winter(find_winner)
        if find_winner == 1: #Update statistics
            list1[player1 - 1] = list1[player1 - 1] + 1
        elif find_winner == 2:
            list2[player2 - 1] = list2[player2 - 1] + 1
        else:
            pass
        print_two_team_stat(list1, list2) #Report statistics

def find_round_winner(one,two):
    if (one == "Rock" and two == "Scissors") or (one == "Paper" and two == "Rock") or (one == "Scissors" and two == "Paper"):
        return 1 #If team1 player wins, return 1.
    elif (two == "Rock" and one == "Scissors") or (two == "Paper" and one == "Rock") or (two == "Scissors" and one == "Paper"):
        return 2 #If team2 player wins, return 2.
    else:
        return 0 #If the players tie, return 0.

def report_winter(find_winner): #Display which team wins, or both teams tie.
    if find_winner == 1:
        print("Team 1 wins.")
    elif find_winner == 2:
        print("Team 2 wins.")
    else:
        print("Both teams tie.")
    print("Update Team Stats:")

def play_all_rounds(r,list1,list2): #Repetitively play rock, paper and scissors for r rounds.
    print("Playing...")
    for i in range(1,r+1):
        print(f"Round {i}")
        play_one_round(list1, list2)
        print("")

def find_final_winner(list1,list2):
    if sum(list1) > sum(list2):
        return 1,sum(list1),sum(list2)
    elif sum(list2) > sum(list1):
        return 2,sum(list2),sum(list1)
    else:
        return 0,sum(list1),sum(list2)
#Show Result
list1 = initialize_list(p)
list2 = initialize_list(p)
print("Initializing...")
print_two_team_stat(list1,list2)
play_all_rounds(r,list1,list2)
print("Game over...")
a,b,c = find_final_winner(list1,list2)
print(f"Team {a} wins.")
print(f"Final scores: {b} vs. {c}")