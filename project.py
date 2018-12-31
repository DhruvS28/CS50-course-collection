import pygame
import math, random, sys, time
from pygame.locals import *


# Display
s_width = 1000
s_heigth = 666
HW, HH = s_width // 2, s_heigth // 2

deaths = 0

# initialise display
pygame.init()
CLOCK = pygame.time.Clock()
CLOCK1 = pygame.time.Clock()
win = pygame.display.set_mode((s_width, s_heigth))
pygame.display.set_caption("Amazing Escape")
FPS = 120

bg = pygame.image.load("star.jpg").convert_alpha()
maze = pygame.image.load("Maze.png").convert_alpha()
maze_mask = pygame.mask.from_surface(maze)
maze_rect = maze.get_rect()
ox = HW - maze_rect.center[0]
oy = HH - maze_rect.center[1]

food1 = pygame.image.load("food1.png").convert_alpha()
water1 = pygame.image.load("water1.png").convert_alpha()

food = pygame.image.load("food.png").convert_alpha()
water = pygame.image.load("water.png").convert_alpha()

guydown = pygame.image.load("down.png").convert_alpha()

guy_mask = pygame.mask.from_surface(guydown)
guy_rect = guydown.get_rect()

#maze = pygame.transform.scale(maze, (12, 10))
#guydown = pygame.transform.scale(guydown, (12, 10))

guy_color = guydown

class alpha(object):
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = 100
		self.height = 20
		self.width1 = 100
		self.vel = 1.6
		self.box = (self.x, self.y, 22, 22)

	def draw(self, win):
		rect = pygame.draw.rect(win, (220,180,135), (390, 420, 100, 20))
		rect1 = pygame.draw.rect(win, (30,214,255), (390, 420, alp.width, alp.height))

	def draw1(self, win):
		rect2 = pygame.draw.rect(win, (190,145,145), (390, 330, 100, 20))
		rect3 = pygame.draw.rect(win, (210,105,30), (390, 330, alp.width1, alp.height))

class beta(object):
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height

	def draw(self, win):
		line = pygame.draw.rect(win, (255,100, 250), (beta.x, beta.y, 20, 2))


font = [pygame.font.SysFont('bookman old style', 18 ,True), pygame.font.SysFont('bookman old style', 20 ,True), \
		pygame.font.SysFont('bookman old style', 48 ,True, True)]

text1 = font[0].render("WATER", 1, (50, 100, 255))
text2 = font[1].render("FOOD", 1, (160, 80, 45))
finish = font[2].render("CONGRATULATIONS! YOU WIN !!!", 1, (160, 80, 45))

beta = beta(520, 330, 24, 24)
alp = alpha(430, 250, 100, 20)

# mainloop

while True:
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE) or (event.type == finish):
			pygame.quit()
			sys.exit()

#while True:
#	events()
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and alp.x > alp.vel:
		alp.x -= alp.vel

	if keys[pygame.K_RIGHT] and alp.x < s_width - 20:
		alp.x += alp.vel

	if keys[pygame.K_UP] and alp.y > alp.vel:
		alp.y -= alp.vel

	if keys[pygame.K_DOWN] and alp.y < s_heigth - 20:
		alp.y += alp.vel

	mx, my = alp.x, alp.y

	offset = (round(mx - ox), round(my - oy))
	result = maze_mask.overlap(guy_mask, offset)
	if keys[pygame.K_LEFT] and result:
			alp.x = alp.x + alp.vel

	if keys[pygame.K_RIGHT] and result:
		alp.x = alp.x - alp.vel

	if keys[pygame.K_UP] and result:
		alp.y = alp.y + alp.vel

	if keys[pygame.K_DOWN] and result:
		alp.y = alp.y - alp.vel

	#if beta.x = 480 and beta.y = 25:

	pygame.time.delay(10)
	B= False
	C= False

	if 0 < alp.width:
		alp.width = alp.width - 0.1
	# WATER
	if (380 < alp.x < 622 and 215 < alp.y < 455) or \
		(258-24 < alp.x < 258+24 and 490-22 < alp.y < 490+22) or \
		(504-24 < alp.x < 504+24 and 490-22 < alp.y < 490+22) or \
		(287-24 < alp.x < 287+24 and 215-22 < alp.y < 215+22) or \
		(350-24 < alp.x < 350+24 and 125-22 < alp.y < 125+22) or \
		(15 -24 < alp.x < 15 +24 and 153-22 < alp.y < 153+22) or \
		(320-24 < alp.x < 320+24 and 29 -22 < alp.y < 29 +22) or \
		(104-24 < alp.x < 104+24 and 613-22 < alp.y < 613+22) or \
		(229-24 < alp.x < 229+24 and 551-22 < alp.y < 551+22) or \
		(659-24 < alp.x < 659+24 and 461-22 < alp.y < 461+22) or \
		(751-24 < alp.x < 751+24 and 247-22 < alp.y < 247+22) or \
		(808-24 < alp.x < 808+24 and 396-22 < alp.y < 396+22) or \
		(961-24 < alp.x < 961+24 and 611-22 < alp.y < 611+20) or \
		(901-24 < alp.x < 901+24 and 428-22 < alp.y < 428+22) or \
		(840-24 < alp.x < 840+24 and 184-22 < alp.y < 184+22) or \
		(807-24 < alp.x < 807+24 and 33 -22 < alp.y < 33 +22):
		if alp.width < 100:
			alp.width = alp.width + 1
		elif alp.width >= 100:
			alp.width
	if alp.width <= 0:
		alp.x = 430
		alp.y = 250
		alp.width = 100
		alp.width1 = 100
		B = True

	if 0 < alp.width1:
		alp.width1 = alp.width1 - 0.1
	# FOOD
	if (380 < alp.x < 622 and 215 < alp.y < 455) or \
		(290-24 < alp.x < 290+24 and 397-24 < alp.y < 397+24) or \
		(475-24 < alp.x < 475+24 and 581-24 < alp.y < 581+24) or \
		(168-24 < alp.x < 168+24 and 275-24 < alp.y < 275+24) or \
		(288-24 < alp.x < 288+24 and 184-24 < alp.y < 184+24) or \
		(107-24 < alp.x < 107+24 and 183-24 < alp.y < 183+24) or \
		(225-24 < alp.x < 225+24 and 30 -24 < alp.y < 30 +24) or \
		(564-24 < alp.x < 564+24 and 149-24 < alp.y < 149+24) or \
		(16 -24 < alp.x < 16 +24 and 488-24 < alp.y < 488+24) or \
		(167-24 < alp.x < 167+24 and 489-24 < alp.y < 489+24) or \
		(442-24 < alp.x < 442+24 and 610-24 < alp.y < 610+24) or \
		(750-24 < alp.x < 750+24 and 335-24 < alp.y < 335+24) or \
		(750-24 < alp.x < 750+24 and 551-24 < alp.y < 551+24) or \
		(930-24 < alp.x < 930+24 and 456-24 < alp.y < 456+24) or \
		(867-24 < alp.x < 876+24 and 92 -24 < alp.y < 92 +24) or \
		(714-24 < alp.x < 714+24 and 151-24 < alp.y < 151+24):
		if alp.width1 < 100:
			alp.width1 = alp.width1 + 1
		elif alp.width1 >= 100:
			alp.width1
	if alp.width1 <= 0:
		alp.x = 430
		alp.y = 250
		alp.width = 100
		alp.width1 = 100
		C = True

	if B or C:
		deaths += 1




	#win.fill((255, 255, 255))
	win.blit(bg, (ox, oy))
	win.blit(maze, (ox, oy))

	win.blit(water1, (540, 390))
	win.blit(water, (258, 490))
	win.blit(water, (504, 490))
	win.blit(water, (287, 215))
	win.blit(water, (350, 125))
	win.blit(water, (15, 153))
	win.blit(water, (320, 29))
	win.blit(water, (104, 613))
	win.blit(water, (229, 551))
	win.blit(water, (659, 461))
	win.blit(water, (751, 247))
	win.blit(water, (808, 396))
	win.blit(water, (961, 611))
	win.blit(water, (901, 428))
	win.blit(water, (840, 184))
	win.blit(water, (807, 33))
	#win.blit(water, (000, 000))

	win.blit(food1, (540, 300))
	win.blit(food, (290, 397))
	win.blit(food, (475, 581))
	win.blit(food, (168, 275))
	win.blit(food, (288, 184))
	win.blit(food, (107, 183))
	win.blit(food, (225, 30))
	win.blit(food, (564, 149))
	win.blit(food, (16, 488))
	win.blit(food, (167, 489))
	win.blit(food, (442, 610))
	win.blit(food, (750, 335))
	win.blit(food, (750, 551))
	win.blit(food, (930, 456))
	win.blit(food, (867, 92))
	win.blit(food, (714, 151))
	#win.blit(food, (000, 000))


	text = font[0].render("DEATHS: " + str(deaths), 1, (255, 100, 50))
	win.blit(text, (510, 215))
	win.blit(text1, (405, 395))
	win.blit(text2, (415, 304))
	finish2 = font[2].render("You only died " + str(deaths) + " times!", 1, (160, 80, 45))

	if 475 < alp.x < 500 and 0 < alp.y < 30:
		print("Win !!!")
		win.fill((50, 50, 50))
		win.blit(finish, (100, 333))
		win.blit(finish2, (200, 400))
		pygame.display.update()
		pygame.time.delay(5000)
		pygame.quit()
		sys.exit()

	alp.draw(win)
	alp.draw1(win)
	win.blit(guy_color, (mx, my))
	if pygame.mouse.get_pressed()[0]:
		pygame.time.delay(200)
		print(pygame.mouse.get_pos())


	pygame.display.update()
	CLOCK.tick(FPS)
	win.fill((0, 0, 0))

