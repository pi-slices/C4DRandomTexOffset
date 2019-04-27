import c4d
from c4d import gui
import random

#Script to randomly offset texture tag x/y values between -100% and 100%
#Written by Pi-Slices
#http://pislices.ca
#April 27th 2019

def main():
    tag = doc.GetActiveTags()
    if not tag:
        gui.MessageDialog('No texture tag selected.')

    for t in tag:
        if not (t.GetType() == 5616):
            gui.MessageDialog('Error: Non-Texture Tag Selected.')
        t[c4d.TEXTURETAG_OFFSETX] = random.uniform(-1,1)
        t[c4d.TEXTURETAG_OFFSETY] = random.uniform(-1,1)
    c4d.EventAdd()
    
if __name__=='__main__':
    main()