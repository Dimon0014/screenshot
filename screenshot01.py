# не подходит нет виртуального захвата
import pyscreenshot as ImageGrab
import os
import time
import json

if __name__ == "__main__":
    with open('coord_snapshot.txt', 'r') as f:  # извлекаем  из файла
        data2 = json.load(f)
    print('', data2)

    im=ImageGrab.grab(bbox=(data2[0],data2[1],data2[2],data2[3])) # X1,Y1,X2,Y2
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    im.show()