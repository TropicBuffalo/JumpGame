import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Game')
clock = pygame.time.Clock()
#screen.fill((255,255,255))

ground = pygame.Surface((800,400))
ground.fill((0,0,0))

sky = pygame.Surface((800,300))
sky.fill((255,255,255))

spike = pygame.Surface((25,50))
spike.fill((0,0,0))
spike_x_pos = 800



player = pygame.Surface((25,25))
player.fill((0,0,0))
player_rect = player.get_rect(topleft=(100,275))
player_gravity = 0
player_y = 200

screen.blit(ground,(0,300))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	#Need to redraw the sky because of spikes
	screen.blit(sky,(0,0))

	#Spike
	spike_x_pos -= 4
	spike_rect = spike.get_rect(topleft=(spike_x_pos,250))
	if spike_x_pos < -25 : spike_x_pos = 800

	#Redraw spike when its out of the screen
	if spike_rect.right <= 0: spike_rect.left = 800
	screen.blit(spike,spike_rect)
	
	#Player
	player_gravity += 1
	player_rect.y += player_gravity
	if player_rect.bottom >= 300: player_rect.bottom = 300
	screen.blit(player,player_rect)


	if player_rect.colliderect(spike_rect):
		print('Collision')

	#Keyboard input
	if event.type ==pygame.KEYDOWN:
		if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
			player_gravity = -18


	pygame.display.update()
	clock.tick(60)