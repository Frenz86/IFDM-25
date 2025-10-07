#versione con input attributi
class Rettangolo:
    def __init__(self,a,b): # ATTRIBUTI
        self.latomagg = a
        self.latomin = b
    def area(self):
        return self.latomagg*self.latomin
    def per(self):
        return (self.latomagg+self.latomin)*2