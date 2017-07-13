import random

class Player:
	def __init__(self, name_in):
		self.name = name_in
		self.at_node = 0
	def move_player(self, node_in): #move the player
		self.at_node = node_in
		


class Board:
	def __init__(self):
		self.players = []
	def add_player(self, player_in):
		self.players.append(player_in)
class Dice:
	def __init__(self):
		self.roll_output = '' #outcome of roll
	def roll(self): #roll the dice and store the outcome
		self.roll_output = random.randrange(10)
	def get_roll(self): #return output of roll
		return self.roll_output

class CAL:
	def __init__(self):
		self.myGUI = ''
		self.myBoard = ''
		
	def Set_GUI(self, in_GUI):
		self.myGUI = in_GUI
	def Run_board(self):
		turns = 0
		winner = False
		my_dice = Dice()
		
		while winner == False: 
			
			for player in self.myBoard.players: 
				#have the players take turn to roll dice
				my_dice.roll() 
				#roll the dice and display it in GUI
				while ((self.myGUI.display_dice(my_dice.get_roll())) == False): #while no clicking
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
	def Create_board(self):
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
		self.myBoard = this_board	
		
