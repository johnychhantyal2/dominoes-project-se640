import random

# Define Classes
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

class CRandom:
    def __init__(self, dominoes):
        self.picked = []
        count = 0
        while count < 10:
            choice = random.choice(dominoes)
            self.picked.append(choice)
            dominoes.remove(choice)
            count = count + 1

class CPlayer:
    def __init__(self, id, tiles):
        self.id = id
        self.tiles = tiles

class CTable:
    def __init__(self, player, snake):
        count = 1
        print("Snake: ", snake, "\n")
        print("Player ", player.id, " Hand:")
        for tile in player.tiles:
            print(count, ": ", tile)
            count = count + 1

# Game Setup
# Select the tiles
# Select the player to play first
# Display messages to welcome players and direct them to play

# Implement Gameplay & Winning Conditions

# Diplay who won and the final snake
