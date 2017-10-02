import pygame #keep namespace
import sys #sys.exit()
import random
# from units import Player,Ball,Enemy
from OOPdisplay import My_display
from baseClass import Hero,Ball,Enemy
MY_FPS=30
screen=My_display()

# hero = Player(55,10) # создаем героя по (x,y) координатам

# he=Enemy(40,screen.HEIGHT-20)
# ball=Ball(40,40)

hero=Hero(width=120,height=10,pos_x=30,pos_y=30)
enemy=Enemy(120,10,50,screen.HEIGHT-20)
left = right = False    # по умолчанию — стоим
ball=Ball(20,20,random.randint(10,screen.WIDTH-20),screen.HEIGHT/2-20)
sprite_list=[]
sprite_list.append(hero)
sprite_list.append(ball)
sprite_list.append(enemy)
group_hero=pygame.sprite.Group()
group_hero.add(hero)
group_enemy=pygame.sprite.Group()
group_enemy.add(enemy)
# group_base.add(ball)
# group_he.add(he)
# group_hero=pygame.sprite.Group()
# group_hero.add(hero)

timer = pygame.time.Clock() #ограничим кол-во кадров
while 1: # Основной цикл программы
	for e in pygame.event.get(): # Обрабатываем события
		if e.type == pygame.QUIT:
			sys.exit()
		if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
			left = True
		if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
		   right = True
		if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
		   right = False
		if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
			left = False    


	if pygame.sprite.spritecollide(ball,group_enemy,False):
		ball.status=True
		ball.y_status=False
	if pygame.sprite.spritecollide(ball,group_hero,False):
		ball.status=False
		ball.y_status=True


	text=pygame.font.Font(None,25).render("We are:{score}".format(score=ball.score),True,[255,0,255])
	if ball.score[0]>=10 or ball.score[1]>=10:
		text=pygame.font.Font(None,25).render("game over:{score}".format(score=ball.score),True,[255,0,255])
		screen.screen.blit(screen.bg, (0,0))
		screen.screen.blit(text,[screen.HEIGHT/2,screen.HEIGHT/2])
		pygame.display.update()
		pygame.time.delay(9000)
		sys.exit()

	screen.Mblit(screen.bg,(0,0))      # Каждую итерацию необходимо всё перерисовывать        

	hero.update(left, right,0,screen.WIDTH)
	for i in sprite_list:
		i.draw(screen.screen)
	ball.update(screen.WIDTH,screen.HEIGHT)
	enemy.update(ball.rect.x,screen.WIDTH-enemy.width)
	# print(ball.xvel,ball.yvel,ball.rect.x,ball.rect.y)	

	screen.Mblit(text,[10,screen.HEIGHT/2])


	pygame.display.update()     # обновление и вывод всех изменений на экран
	timer.tick(MY_FPS)