import pgzrun

WIDTH = 640

box = Rect((50,50), (100,100)) # 50,50 is x,y coordinates, 100,100 is len and breath
box2 = Rect((150,150), (130,30))
def draw():
    screen.fill ('white') # white background
    screen.draw.filled_rect(box, 'red') # Red box
    screen.draw.filled_rect(box2, 'blue')

def update():
    #checks for boundary
    if box.x>WIDTH:
        box.x = 0
        box2.y = 0
        #moves box 3 pixels to the right in every frame
    box.x +=5
    box2.x  +=5
    
pgzrun.go()