class Yatzy:

    @staticmethod
    def chance(*dice):
        score = 0
        for die in dice:
            score += die
        return score

    @staticmethod
    def yatzy(dice):
        if dice.count(dice[0]) == 5:
                return 50
        return 0

    @staticmethod
    def ones(*dice):
        ONE = 1
        return dice.count(ONE) * ONE


    @staticmethod
    def twos(*dice):
        TWO = 2
        score = 0
        for die in dice:
            if die == TWO:
                score = score + TWO
        return score


    @staticmethod
    def threes( d1,  d2,  d3,  d4,  d5):
        s = 0
        if (d1 == 3):
             s += 3
        if (d2 == 3):
             s += 3
        if (d3 == 3):
             s += 3
        if (d4 == 3):
             s += 3
        if (d5 == 3):
             s += 3
        return s
    

    def __init__(self, d1, d2, d3, d4, _5):
        self.dice = [0]*5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = _5
    
    def fours(self):
        sum = 0
        for at in range(5):
            if (self.dice[at] == 4): 
                sum += 4
        return sum
    

    def fives(self):
        s = 0
        i = 0
        for i in range(len(self.dice)): 
            if (self.dice[i] == 5):
                s = s + 5
        return s
    

    def sixes(self):
        sum = 0
        for at in range(len(self.dice)): 
            if (self.dice[at] == 6):
                sum = sum + 6
        return sum
    
    @staticmethod
    def pair(*dice):
        PAIR = 2
        for numero in range(6, 0, -1):
            if dice.count(numero) >= 2:
                return PAIR * numero
        return 0


    @staticmethod
    def two_pair(*dice):
        PAIR = 2
        pairs = 0
        total = 0
        for numero in range(6, 0, -1):
            if dice.count(numero) >= 2:
                pairs += 1
            if pairs == 2:
                return total
        return 0


    @staticmethod
    def four_of_a_kind( _1,  _2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[_1-1] += 1
        tallies[_2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        for i in range(6):
            if (tallies[i] >= 4):
                return (i+1) * 4
        return 0
    

    @staticmethod
    def three_of_a_kind( d1,  d2,  d3,  d4,  d5):
        t = [0]*6
        t[d1-1] += 1
        t[d2-1] += 1
        t[d3-1] += 1
        t[d4-1] += 1
        t[d5-1] += 1
        for i in range(6):
            if (t[i] >= 3):
                return (i+1) * 3
        return 0
    

    @staticmethod
    def smallStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[0] == 1 and
            tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1):
            return 15
        return 0
    

    @staticmethod
    def largeStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1
            and tallies[5] == 1):
            return 20
        return 0
    

    @staticmethod
    def fullHouse( d1,  d2,  d3,  d4,  d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1

        for i in range(6):
            if (tallies[i] == 2): 
                _2 = True
                _2_at = i+1
            

        for i in range(6):
            if (tallies[i] == 3): 
                _3 = True
                _3_at = i+1
            

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0
