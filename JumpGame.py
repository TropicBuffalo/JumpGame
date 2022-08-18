import pygame
from sys import exit
from random import randint

#Calculating score based on time spent in game
#Need to convert gametime to string for it to render
def display_score():
	gametime = int(pygame.time.get_ticks()/1000) - start_time
	score_surface = my_font.render(f'{gametime}', False, (0,0,0))
	score_rect = score_surface.get_rect(center = (750,50))
	screen.blit(score_surface,score_rect)
	return gametime

#Function to handle movement of obstacles, draw them,
#and delete them when they leave the screen
def obstacle_movement(obstacle_list):
	if obstacle_list:
		for obstacle_rect in obstacle_list:
			obstacle_rect.x -= 5

			screen.blit(spike,obstacle_rect)

		obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
		return obstacle_list
	else : return []

#Return False if collision is detected between player and any object in the list
def collisions(player, obstacles):
	if obstacles:
		for obstacle_rect in obstacles:
			if player.colliderect(obstacle_rect): return False
	return True

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Game')
clock = pygame.time.Clock()

#Variable to reset score every game
start_time = 0
#Variable to store score for game over screen
score = 0

#Game state, is the game running or not
game_state = True

my_font = pygame.font.SysFont('Verdana', 30)

#Game over text, make a rect to position it more nicely
game_over = my_font.render("Game over", True, (0,0,0))
game_over_rect = game_over.get_rect(center=(400,130))
restart_game = my_font.render("Press space to restart", True, (0,0,0))
restart_rect = restart_game.get_rect(center=(400,220))

ground = pygame.Surface((800,400))
ground.fill((0,0,0))

sky = pygame.Surface((800,300))
sky.fill((255,255,255))

#Timer
obstacle_timer = pygame.USEREVENT +1
pygame.time.set_timer(obstacle_timer,1500)

#Obstacles
spike = pygame.Surface((25,50))
spike_rect = spike.get_rect(topleft=(800,250))
spike.fill((0,0,0))

obstacle_rect_list = []

#Player
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

		#Insert spike rect objects into a list to be drawn,based on a timer
		if event.type == obstacle_timer and game_state:
			if randint(0,2):
				obstacle_rect_list.append(spike.get_rect(topleft=(randint(900,1100),250)))
			else:
				obstacle_rect_list.append(spike.get_rect(topleft=(randint(900,1100),200)))

	#Experiment with game state, is it running otherwise white screen
	if game_state:
		#Need to redraw the sky and ground because of spikes / game states
		screen.blit(sky,(0,0))
		screen.blit(ground,(0,300))

		#Need to render the score after redrawing the sky so it shows properly
		score = display_score()
		
		#Player
		player_gravity += 1
		player_rect.y += player_gravity
		if player_rect.bottom >= 300: player_rect.bottom = 300
		screen.blit(player,player_rect)

		#Update the list of obstacles
		obstacle_rect_list = obstacle_movement(obstacle_rect_list)

		#Check the list for collisions with player
		game_state = collisions(player_rect, obstacle_rect_list)

		#Keyboard input
		if event.type ==pygame.KEYDOWN:
			if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
				player_gravity = -18

	else:
		#Game over screen, display score
		screen.fill((255,255,255))
		screen.blit(game_over, game_over_rect)
		screen.blit(restart_game,restart_rect)
		start_time = int(pygame.time.get_ticks()/1000)

		#On Game Over clear the obstacle list, reset the player to original position
		obstacle_rect_list.clear()
		player_rect.topleft = (100,275)
		player_gravity = 0


		score_gameover = my_font.render(f'Your score: {score}',False,(0,0,0))
		score_gameover_rect = score_gameover.get_rect(center=(400,180))
		screen.blit(score_gameover,score_gameover_rect)

		#Restart the game
		if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
			game_state = True
			spike_rect.left = 800
			start_time = int(pygame.time.get_ticks()/1000)

	pygame.display.update()
	clock.tick(60)