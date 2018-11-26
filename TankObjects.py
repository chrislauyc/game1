import time
class Object:
    def __init__(self):
        #dimension is a list [x,y]
        #orientation is the initial orientation
        self.x_coor = 50
        self.y_coor = 50
        self.orientation = None
        self.dimensions = None
    def Get_shape(self): #get the dimensions relative to the center
        if self.orientation == "UP" or self.orientation == "DOWN":
            x_dimension = self.dimensions[0]
            y_dimension = self.dimensions[1]
        elif self.orientation == "LEFT" or self.orientation == "RIGHT":
            x_dimension = self.dimensions[1]
            y_dimension = self.dimensions[0]
        elif self.orientation == None: #this is for projectile
            x_dimension = self.dimensions[0]
            y_dimension = self.dimensions[1]
        else:
            ""#error
        x1 = self.x_coor - x_dimension/2
        x2 = self.x_coor + x_dimension/2
        y1 = self.y_coor - y_dimension/2
        y2 = self.y_coor + y_dimension/2
        return (x1,x2,y1,y2)
    def Set_position(self,x_coor,y_coor):
        self.x_coor = x_coor
        self.y_coor = y_coor
class Moving_object(Object):
    def __init__(self):
        Object.__init__(self)
        self.speed_x = 0
        self.speed_y = 0
        self.x_boundary = (None,None)
        self.y_boundary = (None,None)
        self.time = time.time()
        self.prev_x = self.x_coor #store the last position
        self.prev_y = self.y_coor
    def Set_speed(self,speed=(0,0)):#first calculate the position, then set new speed.
        #coor is a tuple (x,y)
        #seconds is a number
        #speed is a number
        self.Get_position()#get the position at the moment
        self.speed_x = speed[0]#assign new speed
        self.speed_y = speed[1]
    def Update_position(self):
        seconds_passed = time.time()-self.time
        self.time = time.time()#reset clock
        self.x_coor = self.speed_x*seconds_passed+self.x_coor
        self.y_coor = self.speed_y*seconds_passed+self.y_coor
    def Get_position(self): #first get time passed, then calculate the new position. SHould have called update position
        #direction "left", "right", "up", "down"
        #fix this
        display_x = int(self.x_coor-self.dimensions[0]/2)
        display_y = int(self.y_coor-self.dimensions[1]/2)
        return display_x, display_y, self.orientation
    def Collision_detection(self,obj_shape):
        #obj_shape is the dimension of other object
        Bx1,Bx2,By1,By2 = obj_shape
        Ax1,Ax2,Ay1,Ay2 = self.Get_shape()
        cond1 = Ax2 > Bx1 and Ax2 < Bx2 and Ay1 < By2 and Ay1 > By1 #the right upper corner is hitting bottom left corner
        cond2 = Ax1 < Bx2 and Ax1 > Bx1 and Ay1 < By2 and Ay1 > By1 #the left upper corner is hitting bottom right corner
        cond3 = Ax2 > Bx1 and Ax2 < Bx2 and Ay2 > By1 and Ay2 < By2 #the right bottom corner hitting upper left corner
        cond4 = Ax1 < Bx2 and Ax1 > Bx1 and Ay2 > By1 and Ay2 < By2 #the left bottom corner hitting upper right corner
        cond5 = Bx2 > Ax1 and Bx2 < Ax2 and By1 < Ay2 and By1 > Ay1 
        cond6 = Bx1 < Ax2 and Bx1 > Ax1 and By1 < Ay2 and By1 > Ay1 
        cond7 = Bx2 > Ax1 and Bx2 < Ax2 and By2 > Ay1 and By2 < Ay2
        cond8 = Bx1 < Ax2 and Bx1 > Ax1 and By2 > Ay1 and By2 < Ay2
        collision = cond1 or cond2 or cond3 or cond4 or cond5 or cond6 or cond7 or cond8
        if collision: #if coliision occur, set the position back to previous
            self.x_coor = self.prev_x
            self.y_coor = self.prev_y
        else:
            self.prev_x = self.x_coor
            self.prev_y = self.y_coor
        return collision
    def Within_bounds(self):
        x1,x2,y1,y2 = self.Get_shape()
        xmin, xmax = self.x_boundary
        ymin, ymax = self.y_boundary
        if x1 > xmin and x2 < xmax and y1 > ymin and y2 < ymax:
            return True
        else:
            if x1 < xmin:
                self.x_coor += xmin-x1
            if x2 > xmax:
                self.x_coor -= x2-xmax
            if y1 < ymin:
                self.y_coor += ymin-y1
            if y2 > ymax:
                self.y_coor -= y2 - ymax
            return False
class Tank(Moving_object):
    def __init__(self,player):
        #dimensions is a tuple (x,y) specifying the shape
        Moving_object.__init__(self)
        self.player = player
        self.projectile_speed = 200 #pixel per sec
        self.projectile_dimensions = (2,2)
        self.speed = 100 #speed is 10 pixel for second
        self.explosion_i = 0 #index of the explosion animation
        self.respawn_i = 0 #index of the respawn animation
    def Shoot(self):
        if self.orientation == "UP":
            p_speed = (0,-self.projectile_speed)
        elif self.orientation == "DOWN":
            p_speed = (0,self.projectile_speed)
        elif self.orientation == "LEFT":
            p_speed = (-self.projectile_speed,0)
        elif self.orientation == "RIGHT":
            p_speed = (self.projectile_speed,0)
        projectile = Projectile(self,p_speed,self.projectile_dimensions,self.x_boundary,self.y_boundary)
        self.Get_position()
        projectile.Set_position(self.x_coor,self.y_coor)
        return projectile
    def Check_hit(self,projectiles):
        for projectile in projectiles:
            if self != projectile.owner:
                projectile.Update_position()
                p_xcoor,p_ycoor = projectile.x_coor,projectile.y_coor
                x1,x2,y1,y2 = self.Get_shape()
                if p_xcoor > x1 and p_xcoor < x2 and p_ycoor > y1 and p_ycoor < y2:
                    return True,projectile
        return False,None
            
class Projectile(Moving_object):
    def __init__(self,owner,speed,dimensions,x_boundary,y_boundary):
        Moving_object.__init__(self)
        self.owner = owner #the tank it belongs to. 
        self.dimensions = dimensions
        self.Set_speed(speed)
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary