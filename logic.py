import random

## ------Display the 6 numbers at random first string


class Logic:

    def lucklnum(self):
        self.whiteball = []
        for i in range(5):
            self.numberluckal = random.randint(1,20)
            while self.numberluckal in self.whiteball:
                self.numberluckal = random.randint(1, 20)
            self.whiteball.append(self.numberluckal)
            self.whiteball.sort()
        for i in range(1):
            self.ball=random.randint(1,10)
            self.whiteball.append(self.ball)
            return self.whiteball

    ##-----Show the 6 numbers randomly in the second string

    def winNumbers(self):
        self.lotory = []
        for n in range(5):
            self.win_num = random.randint(1, 20)
            while self.win_num in self.lotory:
                self.win_num = random.randint(1, 20)
            self.lotory.append(self.win_num)
        for i in range(1):
            self.lotory.sort()
            self.winnwer = random.randint(1, 10)
            self.lotory.append(self.winnwer)
            return self.lotory

