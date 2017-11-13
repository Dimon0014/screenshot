import pyscreenshot as ImageGrab
if __name__ == "__main__":
    im=ImageGrab.grab(bbox=(10,10,300,300)) # X1,Y1,X2,Y2
    im.show()