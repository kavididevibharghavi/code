#Aim:program to display vandematharam n times
#date:2/3/23
class DisplayNtimes:
    def __init__(self):
        self.c=1
    def accept(self):
        self.n=int(input("enter the number to display:"))
    def process(self):
        while self.c<=self.n:
              print("vandematharam")
              self.c=self.c+1
#instantiate object:
d=DisplayNtimes()
d.accept()
d.process()
