
class AI:
    def __init__(self):
        self.start_x = 0
        self.start_y = 0
        self.x_dist = 30
        self.y_dist = 50
    
    def set_start_information(self, x, y, size):
        self.start_x = x
        self.start_y = y
        self.fullhex = []
        x_offset = 0
        y_offset = 0
        for i in range(size):
            for s in range(size):
                self.fullhex.append((self.start_x + x_offset, self.start_y + y_offset))
                x_offset += 30
                y_offset += 50
            x_offset -= 30
            y_offset += 50


    def wincheker(self, hexpos_in, hexcolor_in,size):
        index = []
        for point in self.fullhex[0:size]:
            for s in hexpos_in:
                if(hexpos_in[s][0] - 60 < point[0] and hexpos_in[s][0] + 0 > point[0]
                    and hexpos_in[s][1] - 40 < point[1] and hexpos_in[s][1] + 10 > point[1]) and hexcolor_in[s] == "red":
                    index.append = self.fullhex.index(point)
        for i in index:
                    
                



    def bot(self, fullhex_in, hexpos_in, hexcolor_in):
        for fullhex in fullhex_in:
            for hexpos in hexpos_in:
                if(fullhex[0] - 60 < hexpos[0] and fullhex[0] + 0 > hexpos[0]
                and fullhex[1] - 40 < hexpos[1] and fullhex[1] + 10 > hexpos[1]):
                    pass