import pygame
from pygame.locals import *
import random

size = width, height = (1200, 800)
road_width = int(width/1.6)
roadline_width = int(width/80)
right_lane = width/2 + road_width/4
left_lane = width/2 - road_width/4
speed = 1

pygame.init()
running = True
# set window size
screen = pygame.display.set_mode(size)
# set title
pygame.display.set_caption("Tyyo's Driving Game")
# set background color
screen.fill((200, 200, 0))
# apply changes
pygame.display.update()

# load Player Car
car = pygame.image.load("playercar.png")
car_loc = car.get_rect()
car_loc.center = right_lane, height*0.8

# load NPC Car
car2 = pygame.image.load("npccar.png")
car2_loc = car.get_rect()
car2_loc.center = left_lane, height*0.2

counter = 0
# game loop
while running:
    counter += 1
    if counter == 5000:
        speed += 0.15
        counter = 0
        print("level up", speed)
    # animate NPC
    car2_loc[1] += speed
    if car2_loc[1] > height:
        if random.randint(0, 1) == 0:
            car2_loc.center = right_lane, -200
        else:
            car2_loc.center = left_lane, -200
    # end game
    if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1] - 250:
        print("GAME OVER! CAR WRECK!!!")
        break

    # listening for events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(road_width/2), 0])
            if event.key in [K_d, K_RIGHT]:
                car_loc = car_loc.move([int(road_width/2), 0])
    # draw graphics
    pygame.draw.rect(
        screen,
        (50, 50, 50),
        (width/2-road_width/2, 0, road_width, height))

    pygame.draw.rect(
        screen,
        (255, 255, 60),
        (width/2 - roadline_width/2, 0, roadline_width, height))

    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width/2 - road_width/2 + roadline_width*2, 0, roadline_width, height))

    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width/2 + road_width/2 - roadline_width*3, 0, roadline_width, height))

    screen.blit(car, car_loc)
    screen.blit(car2, car2_loc)
    pygame.display.update()


pygame.quit()
