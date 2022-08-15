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


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	screen.blit(ground,(0,300))
	screen.blit(sky,(0,0))

	spike_x_pos -= 2
	if spike_x_pos < -25 : spike_x_pos = 800
	screen.blit(spike,(spike_x_pos,250))
	spike_rect = spike.get_rect(topleft=(spike_x_pos,250))

	player_gravity += 1
	player_rect.y += player_gravity
	screen.blit(player,player_rect)




	if player_rect.colliderect(spike_rect):
		print('Collision')


	key = pygame.key.get_pressed()
	if key[pygame.K_SPACE]:
		player_gravity = -20
		print(player_rect.bottom)



	pygame.display.update()
	clock.tick(60)