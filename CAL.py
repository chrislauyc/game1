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
	def move_player(node_in): #move the player
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
	turns = 0
	winner = False
	my_dice = Dice()
	
	while winner == False: 
		
		for player in board_in.players: 
			#have the players take turn to roll dice
			my_dice.roll() 
			#roll the dice and display it in GUI
			while !(GUI.display_dice(my_dice.get_roll)) #while no clicking
				my_dice.roll()
			#receive the result of the roll
			roll_result = my_dice.get_roll()	
			#move the players
			new_position = roll_result + player.at_node
			player.move_player(new_position) #would be great to move the player one by one through the list for a better visual effect
				#move the players through the nodes
				#moving display in GUI
			if player.at_node == 100: #check if there is winner
				winner = True
				break
		turns += 1
		
	#end game. would be great to display the winner
		
	pass
