import pygame, random, glob, time
class TankGUI:
    def __init__(self):
        self.screen = ""
        self.player_tank = ""
        self.enemy_tank = ""
        self.walls = ""
        self.enemy_spawn_loc = [] #list of [x,y]
        self.player_spawn_loc = [] #list of [x,y]
        self.explosion = []
        self.Load_environment()
    def Load_environment(self):#also need to define dimension of the tanks
        pygame.init()
        size = width, height = 805,658
        self.walls = [(0,width),(0,height)]
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("testing")
        img = pygame.image.load('PlayerTank2.gif')
        img = pygame.transform.scale(img, (50,50))
        self.player_tank = img
        img = pygame.image.load('EnemyTank.gif')
        img = pygame.transform.scale(img, (50,50))
        self.enemy_tank = img
        explosion_files = glob.glob("Explosion/*.gif")
        for file in explosion_files:
            img = pygame.image.load(file)
            img = pygame.transform.scale(img,(50,50))
            self.explosion.append(img)
        self.player_spawn_loc = [[10,50],[300,50],[500,50],[10,300],[300,300],[500,300]]#should modify this for different spawn locations
        self.enem_spawn_loc = [[300,300]]#can change
        BLACK = (000,000,000)
        self.screen.fill(BLACK)
        #will add in objects in the environment
    def Config_tanks(self,Players,orientation):
        for Player in Players:
            Player.tank.dimensions = (50,50)
            Player.tank.orientation = orientation
            Player.tank.x_boundary, Player.tank.y_boundary = self.walls
            random_loc = random.choice(self.player_spawn_loc)
            Player.tank.x_coor, Player.tank.y_coor = random_loc
    def New_frame(self):
        BLACK = (000,000,000)
        self.screen.fill(BLACK)
    def Update_frame(self):
        pygame.display.flip()
    def Display_tanks(self,Players,projectiles):
        for Player in Players:
            if Player.state == "alive":
                Player.tank.Update_position()
                Player.tank.Within_bounds() #enforce bounds
                [is_hit,projectile] = Player.tank.Check_hit(projectiles)
                if is_hit:
                    Player.state = "dying"
                    projectiles.remove(projectile)
                [x_coor,y_coor,orientation] = Player.tank.Get_position()
                if orientation == "UP":
                    img = self.player_tank
                elif orientation == "RIGHT":
                    img = pygame.transform.rotate(self.player_tank,270)
                elif orientation == "DOWN":
                    img = pygame.transform.rotate(self.player_tank,180)
                elif orientation == "LEFT":
                    img = pygame.transform.rotate(self.player_tank,90)
                self.screen.blit(img,(x_coor,y_coor))
            elif Player.state == "respawn":
                Player.state = "alive"#will add animation
                random_loc = random.choice(self.player_spawn_loc)
                Player.tank.x_coor, Player.tank.y_coor = random_loc
            elif Player.state == "dying":
                i = Player.tank.explosion_i
                [x_coor,y_coor,orientation] = Player.tank.Get_position()
                if i < len(self.explosion):
                    self.screen.blit(self.explosion[i],(x_coor,y_coor))
                    Player.tank.explosion_i += 1
                else:
                    Player.tank.explosion_i = 0
                    Player.state = "dead"
                    Player.spawn_time = time.time() + 3
            elif Player.state == "dead":
                if time.time() > Player.spawn_time:#it has waited for long enough
                    Player.state = "respawn"
    def Display_projectiles(self,Projectiles):
        for i,Projectile in enumerate(Projectiles):
            Projectile.Update_position()
            if Projectile.Within_bounds():
                [x_coor,y_coor,__] = Projectile.Get_position()
                pygame.draw.circle(self.screen, (250,250,0), [x_coor, y_coor], 2)
            else:
                Projectiles.pop(i)
        
    