import pygame


class My_display():
	def __init__(self):
		self.WIDTH = 800 #Ширина создаваемого окна
		self.HEIGHT = 500 # Высота
		self.DISPLAY = (self.WIDTH, self.HEIGHT) # Группируем ширину и высоту в одну переменную
		BACKGROUND_COLOR = "#004400"
		pygame.init() # Инициация PyGame, обязательная строчка 
		self.screen = pygame.display.set_mode(self.DISPLAY) # Создаем окошко
		pygame.display.set_caption("do it on python (not js)") # Пишем в шапку
		self.bg = pygame.Surface((self.WIDTH,self.HEIGHT)) # Создание видимой поверхности(как фон)
		self.bg.fill(pygame.Color(BACKGROUND_COLOR))     # Заливаем поверхность сплошным цветом

	def Mblit(self,value,position):
		 self.screen.blit(value, position)


