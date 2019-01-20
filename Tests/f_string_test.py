class F:
    def __init__(self,x,y):
        self.x,self.y=x,y
        return
    def __str__(self):
        return f'x:{self.x},y:{self.y}'
    def __format__(self,s):
        if s=='d':
            return f'x:{int(self.x)},y:{int(self.y)}'
        else:
            #print(s)
            return f'x:{self.x:{s}},y:{self.y:{s}}'
    def __repr__(self):
        return str(self)+',surprise!'

f=F(1.1,5.8)
print(f'{f}')
print(f'{f!r}')
print(f'{f:d}')
print(f'{f:.2f}')
print(f'{f:010.2f}')
