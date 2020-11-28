import sys
sys.path.append("/Invoerscherm")
import Invoerscherm/invoerscherm

def setup():
    if invoerSchermActive:
        invoerscherm.setup()
        
def draw():
    if invoerSchermActive:
        invoerscherm.draw()