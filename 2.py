#Aim:program to display vandematharam 10 times
#date:2/3/23
class Display:
#constructor
    def __init__(self):
        self.c=1
    def process(self):
        while self.c<=10:    #c is instant variable
            print("vandematharam #",self.c)
            self.c=self.c+1
#instantiate object
d=Display()
d.process()
         
