#Aim:program to read a number and check weather it is divisble by 2 and 5 
#date:2/3/23
class DisplayNumbers:
    def accept(self):
        self.n=int(input("enter n value:"))
    def process(self):
        self.r=self.n%2 or self.n%5
        if self.r==0:
            print(" divisible")
        else:
            print("not divisible")
d=DisplayNumbers()
d.accept()
d.process()
            
