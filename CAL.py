import random
import GUI
class Board:
	def __init__(self):
		self.DLL = '' #need to create a DLL 
	def add_node():
		#add nodes to create a board
		#add connections between nodes
		pass		
class Player:
	def __init__(self, name_in):
		self.name = name_in
		self.at_node = 0
	def change_node(node_in):
		self.at_node = node_in
		

def Create_board():
	#implement the construction of randomly generated board
	#create board. Do this later
	#create players
	this_board = Board()
	player1 = Player('Nicole')
	this_board.add_player(player1)
	player2 = Player('Chris')
	this_board.add_player(player2)
	player3 = Player('Josh')
	this_board.add_player(player3)
	player4 = Player('Meredith')
	this_board.add_player(player4)
		
	
	return this_board #return board "main will be holding the board"
class Board:
	def __init__(self):
		self.players = []
	def add_player(player):
		self.players.append(player)
class Dice:
	def __init__(self):
		self.roll_output #outcome of roll
	def roll(): #roll the dice and store the outcome
		self.roll_output = random.randrange(10)
	def get_roll(): #return output of roll
		return self.roll_output
def Run_board(board_in):
	
	#have the players take turn to roll dice
	turns = 0
	winner = False
	while winner == False: 
		#roll the dice and display it in GUI
			#receive the result of the roll
		#move the players
		for player in board_in.players:
			if player.at_node == 100:
				winner = True
				break
		
		
	#end game	
		
	pass
