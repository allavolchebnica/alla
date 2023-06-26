from pygame import *
speed=6
y1,y2=150,150
x1,x2=50,650
FPS=60
window=display.set_mode((700,500))
display.set_caption('Пинг-понг')
background=transform.scale(image.load('2_e5819e5cff145761bc7d3bb7dfdce4c7.png'), (700,500))
window_width = 700
tomato = 'png-transparent-tomato-soup-tomato-juice-tomato.png'
pregrada1 = 'png-clipart-shovel-shovel.png'
pregrada2 = 'png-clipart-shovel-shovel.png'
xx = 150
yy = 350
clock = time.Clock()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(65,65))
        self.speed_y=player_speed
        self.speed_x=player_speed
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
        
class Player_pravo (GameSprite):
    def update(self):
        keys_pressed=key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y>5:
            self.rect.y-=self.speed
        if keys_pressed[K_DOWN] and self.rect.y<395:
            self.rect.y+=self.speed
        self.reset()

class Player_levo (GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y>5:
            self.rect.y-=self.speed
            self.reset()
        if keys_pressed[K_s] and self.rect.y<395:
            self.rect.y+=self.speed
            self.reset()
        self.reset()

class Tomato (GameSprite):
    def update(self, Player_levo, Player_pravo):
        if not(self.rect.x<=0) and (not(self.rect.x>=700)):
            self.rect.x+=self.speed_x
        else:
            self.speed_x*=-1
            self.rect.x+=2*self.speed_x
        if not(self.rect.y<=0) and (not(self.rect.y>=500)):
            self.rect.y+=self.speed_y
        else:
            self.speed_y*=-1
            self.rect.y+=2*self.speed_y
        if sprite.collide_rect(self, Player_levo) or sprite.collide_rect(self, Player_pravo):
            self.speed_x*=-1
            self.rect.x+=self.speed_x
        self.reset()   

pl2 = Player_levo(pregrada1,0,250,5)
pl1 = Player_pravo(pregrada1,650,250,5)
tomat = Tomato(tomato,350,250,5)

finish=False
game=True
while game:
    window.blit(background,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game=False
    if finish != True:
        pl1.update()
        pl2.update()
        tomat.update(pl2,pl1)
        
    display.update()
    clock.tick(FPS)
