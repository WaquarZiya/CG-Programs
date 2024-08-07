import pygame, random

screen_width = 1300
screen_height = 650
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Animation Effect")

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

num_objs = 10
objs = []

for _ in range(num_objs):
    x = random.randint(50, screen_width - 50)
    y = random.randint(50, screen_height - 50)
    radius = random.randint(10, 60)
    color = random.choice([red, green, blue])
    speedX = random.randint(-5, 5)
    speedY = random.randint(-5, 5)
    objs.append({'x':x, 'y':y, 'radius':radius, 'color':color, 'speedX':speedX, 'speedY': speedY})

running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(white)

    for obj in objs:
        obj['x'] += obj['speedX']
        obj['y'] += obj['speedY']

        if obj['x'] - obj['radius'] < 0 or obj['x'] + obj['radius'] > screen_width:
            obj['speedX'] = -obj['speedX']
        if obj['y'] - obj['radius'] < 0 or obj['y'] + obj['radius'] > screen_height:
            obj['speedY'] = -obj['speedY']

        pygame.draw.circle(screen, obj['color'], (obj['x'], obj['y']), obj['radius'])

    pygame.display.flip()
    clock.tick(60)