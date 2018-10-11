class Node(object):

    def __init__(self, data=0, x_coord=0, y_coord=0):
        self.data = data
        self.x = x_coord
        self.y = y_coord
        
    def get_data(self):
        return self.data

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

