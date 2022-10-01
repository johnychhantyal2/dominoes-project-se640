# Import necessary libraries
import random
import time

# Define Classes
# CDominoes - contains the data structure with pieces
class CDominoes:
    def __init__(self):
        self.dominoes = [
            [0,0],
            [1,1], [1,0],
            [2,2], [2,1], [2,0],
            [3,3], [3,2], [3,1], [3,0],
            [4,4], [4,3], [4,2], [4,1], [4,0],
            [5,5], [5,4], [5,3], [5,2], [5,1], [5,0],
            [6,6], [6,5], [6,4], [6,3], [6,2], [6,1], [6,0]
        ]

# CRandom - as sorting approach for the sequence that the domino pieces will be shown/picked
class CRandom:
    def __init__(self, dominoes):
        self.picked = []
        count = 0
        while count < 10:
            choice = random.choice(dominoes)
            self.picked.append(choice)
            dominoes.remove(choice)
            count = count + 1

# CPlayer - to select a randomly picked and sequentially show the selected pieces
class CPlayer:
    def __init__(self, id, tiles):
        self.id = id
        self.tiles = tiles

# CTable - to show/display the sorted pieces
class CTable:
    def __init__(self, player, snake):
        count = 1
        print("Snake: ", snake, "\n")
        print("Player ", player.id, " Hand:")
        for tile in player.tiles:
            print(count, ": ", tile)
            count = count + 1

# Game Setup
# Selecting the tiles
tiles = CDominoes()

firstPick = CRandom(tiles.dominoes)
secondPick = CRandom(tiles.dominoes)

firstPlayer = CPlayer("1", firstPick.picked)
secondPlayer = CPlayer("2", secondPick.picked)

startingTile = random.choice(tiles.dominoes)
tiles.dominoes.remove(startingTile)
snake = [startingTile]
head = startingTile[0]
tail = startingTile[1]

# Selecting the player to play first
currentPlayer = random.choice([firstPlayer, secondPlayer])

print("\nWelcome to Dominoes!")
print("Let's play!\n")
print("Randomly selecting turn order...")
time.sleep(2)
print("Player ", currentPlayer.id, " will go first!")
print("\nRandomly picking Snake and Player Hands...\n")
time.sleep(2)

# Implement Gameplay & Winning Conditions

# Diplay who won and the final snake
