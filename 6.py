#Aim:program to display numbers from final value to intial value 
#date:2/3/23
class DisplayNumbers:
    def accept(self):
        self.i=int(input("enter the initial value:"))
        self.f=int(input("enter the final value:"))
    def process(self):
        while self.f>=self.i:
            print(self.f,end=' ')
            self.f=self.f-1
d=DisplayNumbers()
d.accept()
d.process()
