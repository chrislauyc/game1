import random, GUI, Node, pygame, numpy

class Player:
    def __init__(self, name_in):
        self.name = name_in
        self.at_node = 1
    def move_player(self, node_in): #move the player
        self.at_node = node_in #add options to move later also allow back or forward movement
class Board:
    def __init__(self):
        self.board = numpy.empty(100, dtype=object)
        self.players = []
    def add_player(self, player_in):
        self.players.append(player_in)
    def load_board(self):
        #start at 100 on map (top left)
        x_coord = 35#to 650
        y_coord = 695#to 0
        
        k=0
        for i in range (0,10):#rows
            for j in range(0,10):#columns
                #hard code the map with shoots and ladders
                data = k;
                if k == 1:
                    data = 38
                elif k == 4:
                    data = 14
                elif k == 9:
                    data = 31
                elif k == 16:
                    data = 6
                elif k == 21:
                    data = 42
                elif k == 28:
                    data = 84
                elif k == 36:
                    data = 44
                elif k == 47:
                    data = 26
                elif k == 49:
                    data = 11
                elif k == 51:
                    data = 67
                elif k == 56:
                    data = 53
                elif k == 62:
                    data = 19
                elif k == 64:
                    data = 60
                elif k == 71:
                    data = 91
                elif k == 80:
                    data = 100
                elif k == 87:
                    data = 24
                elif k == 93:
                    data = 73
                elif k == 95:
                    data = 75
                elif k == 98:
                    data = 78
                
                self.board[k] = Node.Node(data, x_coord, y_coord)
                 #increment position
                if j ==0:
                    y_coord -= 658//10
                elif i%2 == 1:#odd rows
                    x_coord -= 650//10
                elif i%2 == 0:#even rows
                    x_coord += 650//10
                
                k+=1
                
        
class Dice:
    def __init__(self):
        self.roll_output = -1 #outcome of roll
    def roll(self): #roll the dice and store the outcome
        self.roll_output = random.randrange(7)
    def get_roll(self): #return output of roll
        return self.roll_output
class CAL:
    def __init__(self):
        self.myGUI = GUI.GUI()
        self.myBoard = ''
        self.my_dice = Dice()
        
    def Handle_events(self, event, player):
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_r:
                self.my_dice.roll()
            elif event.key==pygame.K_a:
                print("you moved backward " + str(self.my_dice.get_roll()))
                player.move_player(player.at_node - self.my_dice.get_roll())
                if player.at_node > 0:
                    player.move_player(self.myBoard.board[player.at_node].get_data())
                if player.at_node < 1:
                    player.move_player(1)
                
            elif event.key==pygame.K_d:
                print("you moved forward " + str(self.my_dice.get_roll()))
                player.move_player(player.at_node + self.my_dice.get_roll())
                if player.at_node < 100:
                    player.move_player(self.myBoard.board[player.at_node].get_data())
                if player.at_node > 100:
                    player.move_player(100)
                
        return
    
    def Run_board(self):#this is the main game loop and GUI loop
        pygame.event.set_allowed(None)
        pygame.event.set_allowed(pygame.KEYDOWN)
        pygame.event.set_allowed(pygame.QUIT)
        turns = 0
        while True:
            for player in self.myBoard.players:
                self.Take_Turn(player)
                if player.at_node == 100: #check if there is winner
                    player.move_player(99)
                    self.End_Game(player.name)
            turns += 1
            
    def Take_Turn(self, player):
        self.myGUI.Run_GUI(self.myBoard.players, player, self.myBoard.board)

        #roll die
        print("Press r to roll")
        event = pygame.event.wait()
        notpressed = True
        while notpressed:
            if event.key == pygame.K_r:
                notpressed = False
                self.Handle_events(event, player)
                break
            event = pygame.event.wait()
            #roll the dice and display it in GUI
        self.myGUI.Display_dice(self.my_dice.get_roll())
        
        #move the players
        while event.key != pygame.K_a and event.key != pygame.K_d:
            event = pygame.event.wait()
            self.Handle_events(event, player)            
        
    def Create_board(self):
        #implement the construction of randomly generated board
        #create board. Do this later
        #create players
        this_board = Board()
        player1 = Player('Joshiepoo')
        this_board.add_player(player1)
        player2 = Player('MereBear')
        this_board.add_player(player2)
        #player3 = Player('Player3')
        #this_board.add_player(player3)
        #player4 = Player('Player4')
        #this_board.add_player(player4)
        self.myBoard = this_board
        self.myBoard.load_board()
        
    def End_Game(self, winner):
        self.myGUI.Run_GUI(self.myBoard.players, self.myBoard.players[0], self.myBoard.board)
        self.myGUI.Display_winner(winner)
