seed = 1
def randomizer(seed, x, min, max):
        seed = (seed*73493+21546)%100000
        return min + seed %max

print(randomizer(seed, 10, 1, 121))
seed = randomizer(seed, 10, 1,121)
print(randomizer(seed, 10, 1, 121))
seed = randomizer(seed, 10, 1,121)
print(randomizer(seed, 10, 1, 121))
seed = randomizer(seed, 10, 1,121)
print(randomizer(seed, 10, 1, 121))
seed = randomizer(seed, 10, 1,121)
print(randomizer(seed, 10, 1, 121))

def bot(self, hexpos_in, hexcolor_in, size):
     falgsmassiv = []
        hexcolor = hexcolor_in.copy()
        hexpos = hexpos_in.copy()
        counter = 0
        fullhex_in = self.fullhex
        def _bot(fullhex_in, hexpos, hexcolor, counter):
            #assert len(hexpos) <= 121
            
            for fullhex in fullhex_in:
                check = False
                for pos in hexpos: 
                    print(len(hexpos)) #проблема в самом принципе сравнения, сравниваешь каждый друг с другом, а должен найти с нулем коллизий
                    print(counter)
                    if (pos[0] - 60 <= fullhex[0] and pos[0] + 0 >= fullhex[0]
                    and pos[1] - 40 <= fullhex[1] and pos[1] + 10 >= fullhex[1]):
                        check = True
                if not check:
                    #self.wincheker_red(hexpos, hexcolor, size)
                    if self.winchecker_blue(hexpos + [fullhex], hexcolor + [not hexcolor[-1]], size):
                        counter+=1
                    elif not self.winchecker_red(hexpos + [fullhex], hexcolor + [not hexcolor[-1]], size):
                        _bot(fullhex_in, hexpos + [fullhex], hexcolor + [not hexcolor[-1]], counter)
        
        countermas = []
        addmas = []

        for fullhex in fullhex_in:
            check = False
            for pos in hexpos:
                #print(pos)
                #print(fullhex)
                if (pos[0] - 60 < fullhex[0] and pos[0] + 0 > fullhex[0]
                and pos[1] - 40 < fullhex[1] and pos[1] + 10 > fullhex[1]):
                    check = True
            if not check:
                addmas.append(fullhex)
                counter = 0
                _bot(fullhex_in, hexpos + [fullhex], hexcolor + [not hexcolor[-1]], counter)
                countermas.append(counter)
        assert len(addmas) != 0
        return addmas[self.maxidx(countermas)]