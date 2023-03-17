#Aim:program to find sum of odd numbers in the range
#date:2/3/23
class DisplayNumbers:
    def __init__(self):
        self.s=0
    def accept(self):
        self.i=int(input("enter the initial value:"))
        self.f=int(input("enter the final value:"))
    def process(self):
         while self.i<=self.f:
             self.r=self.i%2
             if self.r!=0:
               print(self.i)
               self.s=self.s+self.i
             self.i=self.i+1
         print("sum=",self.s)
d=DisplayNumbers()
d.accept()
d.process()
             
