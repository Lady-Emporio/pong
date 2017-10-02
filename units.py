import pygame
MOVE_SPEED = 7
WIDTH = 240
HEIGHT = 20
COLOR =  "#888888"
def saveStatusValue(value):
    if value<0:
        return value
    else:
        return -value

def savePlusValue(value):
    if value>0:
        return value
    else:
        return -value

class Player(pygame.sprite.Sprite):
    def __init__(self, x,y):
        self.y=y
        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0   #скорость перемещения. 0 - стоять на месте
        self.startX = x # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.image = pygame.Surface((WIDTH,HEIGHT))
        self.image.fill(pygame.Color(COLOR))
        self.rect = pygame.Rect(x, self.y, WIDTH, HEIGHT) # прямоугольный объект

    def update(self,  left, right,start,end):
        if self.rect.x<=start and left: #display end and start
            self.xvel = 0
        elif self.rect.x+WIDTH>=end and right: #right side.
            self.xvel = 0         
        elif left:
            self.xvel = -MOVE_SPEED # Лево = x- n
        elif right:
            self.xvel = MOVE_SPEED # Право = x + n
        if not(left or right): # стоим, когда нет указаний идти
            self.xvel = 0
        self.rect.x += self.xvel # переносим свои положение на xvel 
   
    def draw(self, screen): # Выводим себя на экран
        screen.blit(self.image, (self.rect.x,self.y))
        #screen.Mblit(self.image, (self.rect.x,self.y))


class Ball(pygame.sprite.Sprite):
    def __init__(self, x,y):
        self.BALLWIDTH=30
        self.BALLHEIGHT=30
        self.score=[0,0]
        pygame.sprite.Sprite.__init__(self)
        self.xvel = 2   #скорость перемещения.
        self.yvel = 2
        self.image = pygame.Surface((self.BALLWIDTH,self.BALLHEIGHT))
        self.image.fill(pygame.Color("#800080"))
        self.rect = pygame.Rect(x, y, self.BALLWIDTH, self.BALLHEIGHT) # прямоугольный объект

        self.status_hit=False
        self.move=0
        self.move_status=self.move
        self.hit_hero=False
        self.hero_status=self.hit_hero
    def update(self,endBottom,endTop):
        # if self.status_hit==False:
        #     self.yvel =savePlusValue(self.yvel)   
        # if self.status_hit==True:
        #     self.yvel =saveStatusValue(self.yvel)
        
        # if self.rect.y<=0:
        #     self.status_hit=False
        #     self.score[0]+=1
        # elif self.rect.y+self.BALLHEIGHT>=endTop:
        #     self.score[1]+=1
        #     self.status_hit=True

        # if self.rect.x<=0:
        #     self.xvel =savePlusValue(self.xvel)
        # elif self.rect.x+self.BALLWIDTH>=endBottom:
        #     self.xvel =saveStatusValue(self.xvel)
        # else:
        #     self.xvel =self.xvel

        # self.rect.x += self.xvel # переносим свои положение на xvel 
        # self.rect.y += self.yvel

        if self.hit_hero!=self.hero_status:
            self.move+=1
            if self.status_hit==False:
                self.yvel =savePlusValue(self.yvel)
                self.yvel+=1
            if self.status_hit==True:
                self.yvel =saveStatusValue(self.yvel)
                self.yvel -=1
            

            if self.xvel>=0:
                self.xvel+=1
            else:
                self.xvel-=1

            self.rect.x += self.xvel # переносим свои положение на xvel 
            self.rect.y += self.yvel
            if self.move>=6:
                self.move=0
                if self.status_hit==False:
                    self.yvel=2
                if self.status_hit==True:
                    self.yvel=-2
                if self.xvel>=0:
                    self.xvel=2
                else:
                    self.xvel=-2
                


            self.hero_status=self.hit_hero


        if self.status_hit==False:
            self.yvel =savePlusValue(self.yvel)   
        if self.status_hit==True:
            self.yvel =saveStatusValue(self.yvel)
        
        if self.rect.y<=0:
            self.status_hit=False
            self.score[0]+=1
        elif self.rect.y+self.BALLHEIGHT>=endTop:
            self.score[1]+=1
            self.status_hit=True

        if self.rect.x<=0:
            self.xvel =savePlusValue(self.xvel)
        elif self.rect.x+self.BALLWIDTH>=endBottom:
            self.xvel =saveStatusValue(self.xvel)
        else:
            self.xvel =self.xvel




        self.rect.x += self.xvel # переносим свои положение на xvel 
        self.rect.y += self.yvel
          
    def draw(self, screen): # Выводим себя на экран
        screen.blit(self.image, (self.rect.x,self.rect.y))



class Enemy(pygame.sprite.Sprite):
    def __init__(self, x,y):
        self.ENEMYWIDTH=120
        self.ENEMYHEIGHT=20
        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0   #скорость перемещения.
        self.image = pygame.Surface((self.ENEMYWIDTH,self.ENEMYHEIGHT))
        self.image.fill(pygame.Color("#00FFFF"))
        self.rect = pygame.Rect(x, y, self.ENEMYWIDTH, self.ENEMYHEIGHT) # прямоугольный объект

        self.move=0
        self.speed=5
    def update(self,ballX):

        if self.rect.x+(self.ENEMYWIDTH/2)<=ballX:
            self.xvel =self.speed
        elif self.rect.x+(self.ENEMYWIDTH/2)>=ballX:
            self.xvel =-self.speed
        self.move+=self.xvel%1
        if self.move%1==0:
            self.rect.x +=self.move
            self.move=0
        self.rect.x += self.xvel # переносим свои положение на xvel
   
    def draw(self, screen): # Выводим себя на экран
        screen.blit(self.image, (self.rect.x,self.rect.y))

