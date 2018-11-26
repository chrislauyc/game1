class Node(object):

    def __init__(self, data=0, x_coord=0, y_coord=0,mini_game=""):
        self.data = data
        self.x = x_coord
        self.y = y_coord
        self.mini_game = mini_game
    def get_data(self):
        return self.data

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

