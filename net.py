import os
netlist=['tg','wifi']
def net():
     c=int(input())
     b=int(input())-1
     if c==0:
          a=os.popen('netsh interface set interface %s enabled'%netlist[b]).read()
          return
     else:
          #b=int(input())-1
          a=os.popen('netsh interface set interface %s disabled'%netlist[b]).read()
          return
if __name__=='__main__':
     net()
