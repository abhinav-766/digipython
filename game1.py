# run this in terminal -> pip install pgzero
import pgzrun
from random import randint

WIDTH =1000
HEIGHT =800
score = 0
music.play("bombastic")

player = Actor("ironman",(WIDTH//2, HEIGHT//2))
coin = Actor('coin',(randint(50,WIDTH-50),
                     randint(50,HEIGHT-50)))
alien = Actor('alien',(-100,HEIGHT//2,))


ps=5
es=2

def player_movement():
    if keyboard.left:
        player.x -= ps
        player.angle =10
    if keyboard.right:
        player.x += ps
        player.angle =10
    if keyboard.up:
        player.y -= ps    
    if keyboard.down:
        player .y += ps    



def draw():
    screen.fill("white")
    screen.draw.text(
        f"Score:{score}",
        color="black",
        topleft=(10,10),
        fontsize=30

    )
    player.draw()
    coin.draw()
    alien.draw()

def update(dt):
    print(dt)
    player_movement()

pgzrun.go()    