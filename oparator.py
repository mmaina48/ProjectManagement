
class Length:
    def __init__(self,c,m):
        self.c = c
        self.m = m

    def __str__(self):
        return ('Length (%d cm, %d mm)'% (self.c , self.m ))
    def __add__(self, other):
        return (Length(self.c + other.c , self.m + other.m))

ab = Length(2,6)
cd = Length(5,3)
print(ab+cd)