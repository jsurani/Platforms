import pgzrun
WIDTH,HEIGHT = 500,400
alien = Actor("alien")
alien.pos = 250,200
LOSE = True 
floor = ZRect((0,HEIGHT - 100),(200,20))
alien.xspeed = 0
alien.yspeed = 0
GAMEOVER = False

floor.xspeed = 2
floor.yspeed = -1
floor.leftlimit = 0
floor.rightlimit = WIDTH
floor.toplimit = 150
floor.bottomlimit = HEIGHT
SCORE = 0

alien.onground = False

GRAVITY = 0.3
FRICTION = 0.97
def draw():
  if GAMEOVER :
    screen.clear()
    screen.draw.text(" game over " ,center = (WIDTH/2,HEIGHT/2),fontsize = 50)
  else:
    screen.clear()
    alien.draw()
    screen.draw.filled_rect(floor,(255,255,255))
    screen.draw.text("score: " + str(SCORE),(5,5))


def update(): 
  global GAMEOVER
  global SCORE
  if not GAMEOVER:
    alien.yspeed += GRAVITY
    alien.xspeed *= FRICTION
    alien.x += alien.xspeed
    alien.y += alien.yspeed
    if alien.colliderect(floor):
      alien.bottom = floor.top
      alien.onground = True
      alien.yspeed = 0
    if keyboard.left:
      alien.xspeed -= 0.3
    if keyboard.right:
      alien.xspeed += 0.3
    if keyboard.space and alien.onground:
      alien.onground = False
      alien.yspeed = -10
    floor.x += floor.xspeed
    floor.y += floor.yspeed
    if floor.right > floor.rightlimit:
      floor.right = floor.rightlimit
      floor.xspeed = - floor.xspeed
    if floor.left < floor.leftlimit:
      floor.left = floor.leftlimit
      floor.xspeed = - floor.xspeed
    if floor.top < floor.toplimit:
      floor.top = floor.toplimit
      floor.yspeed = - floor.yspeed
    if floor.bottom > floor.bottomlimit:
      floor.bottom = floor.bottomlimit
      floor.yspeed = - floor.yspeed
    SCORE = SCORE + 1

    if alien.y > HEIGHT :
      GAMEOVER = True


pgzrun.go()
