import pygame
import random
def returnMinusValue(value):
	if value<0:
		return value
	else:
		return -value

def returnPlusValue(value):
	if value>0:
		return value
	else:
		return -value

def returnColor():
		r=random.randint(0,255)
		g=random.randint(0,255)
		b=random.randint(0,255)
		return r,g,b

class Base(pygame.sprite.Sprite):
	def __init__(self,width,height,pos_x,pos_y):
		self.width=width;self.height=height;self.pos_x=pos_x;self.pos_y=pos_y
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((self.width,self.height))
		self.r,self.g,self.b=returnColor()
		self.image.fill(pygame.Color(self.r,self.g,self.b))
		self.rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)
		self.colorList=[]
		self.move=4

	def update(self):
		pass
	def draw(self, screen,value=0): # Выводим себя на экран
		screen.blit(self.image, (self.rect.x,self.pos_y))


class Hero(Base):
	def update(self,  left, right,start,end):
		if self.rect.x<=start and left: #display end and start
			speed = 0
		elif self.rect.x+self.width>=end and right: #right side.
			speed = 0         
		elif left:
			speed = -self.move # Лево = x- n
		elif right:
			speed = self.move # Право = x + n
		if not(left or right): # стоим, когда нет указаний идти
			speed = 0
		self.rect.x += speed # переносим свои положение на speed



class Ball(Base):
	def __init__ (self,*arg):
		# super(Base,self).__init__()
		Base.__init__(self,*arg)
		self.hit_hero=self.status=None
		self.yvel=self.xvel=2
		self.x_status=self.y_status=True #if True x+=xvel if False x-=xvel
		self.score=[0,0]

	def update(self,game_w,game_h):
		if self.rect.x+self.width>=game_w:
			self.x_status=False
		elif self.rect.x<=0:
			self.x_status=True

		if self.rect.y+self.height>=game_h:
			self.y_status=False
			self.score[1]+=1
		elif self.rect.y<=0:
			self.y_status=True
			self.score[0]+=1

		if self.hit_hero!=self.status:
			self.yvel=returnPlusValue(self.yvel)+1
			self.xvel=returnPlusValue(self.xvel)+1
			self.hit_hero=self.status
			if self.yvel>=10:
				self.yvel=6
				self.xvel=6

		if self.x_status==True:
			self.xvel=returnPlusValue(self.xvel)
		elif self.x_status==False:
			self.xvel=returnMinusValue(self.xvel)

		if self.y_status==True:
			self.yvel=returnPlusValue(self.yvel)
		elif self.y_status==False:
			self.yvel=returnMinusValue(self.yvel)

		self.rect.x += self.xvel
		self.rect.y += self.yvel

	def draw(self, screen,value=0): # Выводим себя на экран
		self.colorList.append(value)
		if len(self.colorList)>=60:
			self.colorList=[]
			self.r,self.g,self.b=returnColor()
			self.image.fill(pygame.Color(self.r,self.g,self.b))
		screen.blit(self.image, (self.rect.x,self.rect.y))


class Enemy(Base):
	def __init__(self,*arg):
		Base.__init__(self,*arg)
		self.storage=0
	def update(self,ballX,endright):
		self.move=4
		if self.rect.x+(self.width/2)<=ballX:
			self.move =returnPlusValue(self.move)
			if self.rect.x>= endright and self.move>=0:
				self.move=0
		elif self.rect.x+(self.width/2)>=ballX:
			self.move =returnMinusValue(self.move)
			if self.rect.x<=0 and self.move<=0:
				self.move=0
		if self.move!=0:
			self.storage+=self.move%1
			if self.storage%1==0:
				self.rect.x +=self.storage
				self.storage=0


			

		self.rect.x += self.move # переносим свои положение на xvel