#programs on loops
#Aim:program to find factors of the given numbers
#date:3/3/23
#example 6=1,2,3,6
#8=1,2,4,8
class factors:
    def __init__(self):
        self.c=1
    def accept(self):
        self.n=int(input("enter the number:"))
    def process(self):
        while self.c<=self.n:
            self.r=self.n%self.c
            if self.r==0:
              print(self.c,end=' ')
            self.c=self.c+1
d=factors()
d.accept()
d.process()
