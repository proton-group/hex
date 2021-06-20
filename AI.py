
class AI:
    def __init__(self):
        self.start_x = 0
        self.start_y = 0
        self.x_dist = 30
        self.y_dist = 50
        self.winflag = False
    
    def set_start_information(self, x, y, size):
        self.start_x = x
        self.start_y = y
        self.fullhex = []

        for i in range(size):
            x_offset = 0
            y_offset = 0
            for s in range(size):
                self.fullhex.append((self.start_x + x_offset, self.start_y + y_offset))
                x_offset += 30
                y_offset += 50
            self.start_x -= 30
            self.start_y += 50
        #print(len(self.fullhex))


    def wincheker(self, hexpos_in, hexcolor_in, size):
        nextpoint = self.fullhex[0:size]
        def _wincheker(nextpoint, hexpos_in, hexcolor_in, size):
            index = []
            exitflag = False
            for point in nextpoint:
                for s in range(len(hexpos_in)):
                    if(hexpos_in[s][0] - 60 < point[0] and hexpos_in[s][0] + 0 > point[0]
                        and hexpos_in[s][1] - 40 < point[1] and hexpos_in[s][1] + 10 > point[1]) and hexcolor_in[s] == True:
                        index.append(self.fullhex.index(point))
                        if nextpoint[0] in self.fullhex[size*size-size:size*size-2] or nextpoint[1] in self.fullhex[size*size-size:size*size-2]:
                            self.winflag = True

            nextpoint = []
            if len(index) > 0 and not self.winflag:
                for i in index:
                    nextpoint.append(self.fullhex[i+size])
                    nextpoint.append(self.fullhex[i+size-1])
                print(nextpoint)
                _wincheker(nextpoint, hexpos_in, hexcolor_in, size)          
        print(self.fullhex[120])
        _wincheker(nextpoint, hexpos_in, hexcolor_in, size)



    def bot(self, fullhex_in, hexpos_in, hexcolor_in):
        for fullhex in fullhex_in:
            for hexpos in hexpos_in:
                if(fullhex[0] - 60 < hexpos[0] and fullhex[0] + 0 > hexpos[0]
                and fullhex[1] - 40 < hexpos[1] and fullhex[1] + 10 > hexpos[1]):
                    pass