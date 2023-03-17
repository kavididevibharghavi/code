#Aim:program to display 1 to 10 
#date:2/3/23
class DisplayNumbers:
    def __init__(self):
        self.c=1
    def accept(self):
        self.n=int(input("enter the number:"))
    def process(self):
        while self.c<=self.n:
            print(self.c,end=' ')
            self.c=self.c+1
d=DisplayNumbers()
d.accept()
d.process()
    
