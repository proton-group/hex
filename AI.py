import random
from log import createlog
class AI:
    def __init__(self):
        self.start_x = 0
        self.start_y = 0
        self.x_dist = 30
        self.y_dist = 50
        self.winflag = False
        self.winflag_blue = False
        self.winflag_red = False
        self.seed = 1
        random.seed()
    
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
        createlog(str(self.fullhex), "points of playground")
        #print(len(self.fullhex))
    
    def randomizer(self, min, max):
        self.seed = (self.seed*73493+21546)%100000
        return min + self.seed % max

    
    def _winchecker(self, nextpoint, hexpos_in, hexcolor_in, size, winmas, step1, step2, color):
        index = []
        exitflag = False
        for point in nextpoint:
            for s in range(len(hexpos_in)):
                if(hexpos_in[s][0] - 60 < point[0] and hexpos_in[s][0] + 0 >= point[0]
                    and hexpos_in[s][1] - 40 < point[1] and hexpos_in[s][1] + 10 >= point[1]) and hexcolor_in[s] == color:
                    index.append(self.fullhex.index(point))
                    #print(color)
                    #print(index)

        nextpoint = []
        if len(index) > 0 and self.winflag != True:
            for i in index:
                createlog(str(index), "index")
                if i in winmas:
                    createlog("True", "win position found")
                    #print('return')
                    self.winflag = True
                if i+size < len(self.fullhex):
                    nextpoint.append(self.fullhex[i+step1])
                    nextpoint.append(self.fullhex[i+step2])
                #print(nextpoint)
                #print(winmas)
            self._winchecker(nextpoint, hexpos_in, hexcolor_in, size, winmas, step1, step2, color) 
        
            


    def winchecker_red(self, hexpos_in, hexcolor_in, size):
        nextpoint = self.fullhex[0:size]       
        #print(self.fullhex[120])
        self._winchecker(nextpoint, hexpos_in, hexcolor_in, size, [110+i for i in range(size)], size, size-1, True)
        #createlog(str(self.winflag), "wincheck_red return")
        return self.winflag

    def winchecker_blue(self, hexpos_in, hexcolor_in, size):
        idx = 0
        nextpoint = []
        while idx <= size*10:
            nextpoint.append(self.fullhex[idx])
            idx += size
        #print(self.fullhex[120])
        self._winchecker(nextpoint, hexpos_in, hexcolor_in, size, [10+11*i for i in range(size)], 1, 1-size, False)
        createlog(str(self.winflag), "wincheck_red return")
        return self.winflag

    def maxidx(self, mas):
        max = 0
        idx = 0
        for element in mas:
            if element > max:
                idx = mas.index(element)
                max = element
        if idx != 0:
            createlog(str(idx), "not null bot index")
        return idx


    def bot(self, hexpos_in, hexcolor_in, size):
        hexpos = hexpos_in.copy()
        hexcolor = hexcolor_in.copy()
        def _bot(hexpos, hexcolor, size, gensize):
            fullhex = self.fullhex.copy()
            for pos in hexpos:
                if pos in fullhex:
                    fullhex.remove(pos)
            counter = 0
            for i in range(gensize):
                while len(hexpos) < len(self.fullhex):
                    #check = False
                    randhex = fullhex[random.randint(0, len(fullhex)-1)]
                    #while not check:
                        #randhex = self.fullhex[random.randint(0, len(self.fullhex)-1)]
                        #print(randhex)
                        #check = False
                        #for pos in hexpos: 
                            #if (pos[0] - 60 <= randhex[0] and pos[0] + 0 >= randhex[0]
                            #and pos[1] - 40 <= randhex[1] and pos[1] + 10 >= randhex[1]):
                                #check = True
                    hexpos.append(randhex)
                    fullhex.remove(randhex)
                    hexcolor.append(not hexcolor[-1])
                    #print("okay")
                    if self.winchecker_blue(hexpos, hexcolor, size):
                        self.winflag = False
                        counter += 1
                        #print(counter)
                        break
                #return hexpos, hexcolor
                    
            return counter

        countmas = []
        addmas = []

        for fullhex in self.fullhex:
            check = False
            for pos in hexpos:
                if (pos[0] - 60 <= fullhex[0] and pos[0] + 0 >= fullhex[0]
                and pos[1] - 40 <= fullhex[1] and pos[1] + 10 >= fullhex[1]):
                    check = True
            if not check:
                addmas.append(fullhex)
                countmas.append(_bot(hexpos + [fullhex], hexcolor + [not hexcolor[-1]], size, 100))
                #addmas.append(mas[0])
        #assert len(addmas) != 0
        #print("addmas")
        #print(addmas[self.maxidx(countmas)])
        #print(countmas)
        createlog(str(countmas), "massive with count of win position")
        createlog(str(addmas[self.maxidx(countmas)]), "bot return")
        return addmas[self.maxidx(countmas)]
        #return _bot(hexpos, hexcolor, size, 500)
                    
                    
