import getch

global key
while(True):
    key = ord(getch.getch())
    print(key)
    if (key == 27):
        exit(0)