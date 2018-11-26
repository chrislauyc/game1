#mini game
import pygame,TankObjects,TankGUI,math,time
class Player:
    def __init__(self,name):
        self.name = name
        self.tank = TankObjects.Tank(self)
        self.life = 5
        self.kill = []#list of players killed
        self.spawn_time = 0 #sec
        self.keys = {}
        self.key_down = False
        self.state = "alive" #alive, dead,respawn, gameover
    def Set_keys(self,key_list):
        self.keys = {True:[],False:[[key_list[0],"UP"],[key_list[1],"DOWN"],[key_list[2],"LEFT"],
                            [key_list[3],"RIGHT"],[key_list[4],"SHOOT"]]}
    def Key_change(self,key_in,key_down):
        #key_in is a pygame key
        #key_down is a boolean
        #will move keys between True and False lists
        if key_down == True:
            keysF = self.keys[False]
            for i,k in enumerate(keysF):
                if k[0] == key_in:
                    self.keys[True].append(k)
                    keysF.pop(i)
                    return True
        elif key_down == False:
            keysT = self.keys[True]
            for i,k in enumerate(keysT):
                if k[0] == key_in:
                    self.keys[False].append(k)
                    keysT.pop(i)
                    return True
        return False
class Tank_game:
    def __init__(self):
        self.Enemies = []
        self.Players = []
        self.Projectiles = []
        self.GUI = TankGUI.TankGUI()
        
    def Create_game(self):
        #do this for now
        player1 = Player("Chris")
        player1.Set_keys([pygame.K_UP,pygame.K_DOWN,pygame.K_LEFT,pygame.K_RIGHT,pygame.K_RCTRL])
        player2 = Player("Nicole")
        player2.Set_keys([pygame.K_w,pygame.K_s,pygame.K_a,pygame.K_d,pygame.K_e])
        self.Players.append(player1)
        self.Players.append(player2)

    def Run_Tank(self):
        self.GUI.Config_tanks(self.Players,"UP")
        pygame.event.set_allowed(None)
        pygame.event.set_allowed(pygame.KEYDOWN)
        pygame.event.set_allowed(pygame.KEYUP)
        pygame.event.set_allowed(pygame.QUIT)
        
        
        
        event_state = "game"
        max_fps = 50
        while event_state == "game": #update frame
            events = pygame.event.get()
            if len(events) > 0:
                self.Handle_events(self.Players,self.Enemies,events)
            self.GUI.New_frame()
            #sill add check hit and explosion animation
            self.GUI.Display_tanks(self.Players,self.Projectiles)
            self.GUI.Display_projectiles(self.Projectiles)
            self.GUI.Update_frame()
            time.sleep(1/max_fps)
            #update frame
        
        #
    def Check_hit(self):
        #check for hit, add kill,destroy tanks,count down for respawn
        return
    def Handle_events(self,Players,Enemies,events):#update speed, orientation
        for event in events: #loop through events in a queue
            if event.type == pygame.QUIT:
                pygame.quit()
            
            elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP: #in the future, will have the interface config the keys
                key_down = (event.type == pygame.KEYDOWN)
                key_selected = None
                for player in Players: #check the key for each player
                    if player.Key_change(event.key,key_down): #return true if the key change belongs to the player
                        keysT = player.keys[True] #get all the down keys
                        if len(keysT) > 0:
                            key_selected = keysT[0] #pick only the first down key
                            key_label = key_selected[1]#take the text label of the key
                            tank = player.tank
                            if key_label == "UP":
                                tank.Set_speed((0,-tank.speed))
                                tank.orientation = key_label
                            elif key_label == "DOWN":
                                tank.Set_speed((0,tank.speed))
                                tank.orientation = key_label
                            elif key_label == "LEFT":
                                tank.Set_speed((-tank.speed,0))
                                tank.orientation = key_label
                            elif key_label == "RIGHT":
                                tank.Set_speed((tank.speed,0))
                                tank.orientation = key_label
                            elif key_label == "SHOOT" and player.state == "alive":
                                projectile = tank.Shoot()
                                self.Projectiles.append(projectile)
                            break
                        else:
                            player.tank.Set_speed((0,0))
                            break
