import pygame
pygame.init()

win=pygame.display.set_mode((500, 500))
pygame.display.set_caption("Speeder")
x=0
y=0
width=40
height=(40)
vel=5

run=True
while run:
	pygame.time.delay(100)

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False
	keys=pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		x-=vel
	if keys[pygame.K_RIGHT]:
		x+=vel
	if keys[pygame.K_UP]:
		y-=vel
	if keys[pygame.K_DOWN]:
		y+=vel
	if x>=500:
		x=500
	if y>=500:
		y=500
	win.fill((0,0,0))
	pygame.draw.rect(win,(0,255,0),(x,y,width,height))
	pygame.display.update()
pygame.quit()