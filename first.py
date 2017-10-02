import pygame #keep namespace
import sys #sys.exit()
from units import Player,Ball,Enemy
from OOPdisplay import My_display
MY_FPS=30
screen=My_display()

hero = Player(55,10) # создаем героя по (x,y) координатам
left = right = False    # по умолчанию — стоим

he=Enemy(40,screen.HEIGHT-20)
ball=Ball(40,40)

group_he=pygame.sprite.Group()
group_he.add(he)
group_hero=pygame.sprite.Group()
group_hero.add(hero)

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


	if pygame.sprite.spritecollide(ball,group_he,False):
		ball.status_hit=True
		ball.hit_hero=False
	if pygame.sprite.spritecollide(ball,group_hero,False):
		ball.status_hit=False
		ball.hit_hero=True


	text=pygame.font.Font(None,25).render("We are:{score}".format(score=ball.score),True,[255,0,255])
	if ball.score[0]>=10 or ball.score[1]>=10:
		text=pygame.font.Font(None,25).render("game over:{score}".format(score=ball.score),True,[255,0,255])
		screen.screen.blit(screen.bg, (0,0))
		screen.screen.blit(text,[screen.HEIGHT/2,screen.HEIGHT/2])
		pygame.display.update()
		pygame.time.delay(9000)
		sys.exit()

	screen.Mblit(screen.bg,(0,0))      # Каждую итерацию необходимо всё перерисовывать        
	screen.Mblit(text,[10,screen.HEIGHT/2])
	hero.update(left, right,0,screen.WIDTH) # передвижение
	hero.draw(screen.screen) # отображение
	ball.update(screen.WIDTH,screen.HEIGHT) # передвижение
	ball.draw(screen.screen)# отображение
	he.update(ball.rect.x,screen.WIDTH) # передвижение
	he.draw(screen.screen)# отображение


	pygame.display.update()     # обновление и вывод всех изменений на экран
	timer.tick(MY_FPS)