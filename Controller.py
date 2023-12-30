from view import *
from model import *
class controller:
  def __init__(self):
    self.curent=1
    self.last=-1
    self.Algorithm=None
    self.ID=None
  def change(self,x,Algorithm=None,ID=None):
    self.curent=x
    self.Algorithm=Algorithm
    self.ID=ID
  
  def start(self):
    while self.last!=self.curent:
      self.last=self.curent
      if self.curent==1:
        form1(self)
      elif self.curent==2:
        form2(self)
      elif self.curent==3:
        form3(self)
      elif self.curent==5:
        P=solve(self.ID,self.Algorithm)
        B=GetStat(self.ID)
        form5(B,P,self)
      
      else:
        B=GetStat(self.curent)
        form6(B,self)


Admin=controller()
Admin.start()

