
try:
    import colorama
    colorama.init()
except ImportError:
    pass
for i in range(8):
    for j in range(8):
        print("\033[2;3%d;4%dmError!\033[5;0m"%(i,j))  
input()
