#Aim:program to display numbers in the range 
#date:2/3/23
class DisplayNumbers:
    def accept(self):
        self.i=int(input("enter the initial value:"))
        self.f=int(input("enter the final value:"))
    def process(self):
        while self.i<=self.f:
            print(self.i,end=' ')
            self.i=self.i+1
d=DisplayNumbers()
d.accept()
d.process()
