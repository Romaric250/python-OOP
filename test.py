
import time

class Myclass(object):

    def setage(self, num, ):
        self.age = num
   
    def set_fname_and_sname(self, fname, sname):
        self.fname = fname
        self.sname = sname
    def get_time(self,timenow):
        self.time = timenow

        print(timenow.time.now)


    def get_fname_and_sname(self):
        #get the values of the first and second names
        print(self.fname, self.sname)

    def getage(self):
        print(self.age)
    
zack = Myclass()
zack.setage(34)
zack.set_fname_and_sname('Romaric','Lonfonyuy')
zack.get_fname_and_sname()
zack.getage()

