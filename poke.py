import pygame
import requests

num = input("Pokeinput a pokenumber: ")

x = requests.get('https://pokeapi.co/api/v2/pokemon/' + num)

data = [x.json()]
name = (data[0]['forms'][0]['name'])
image = (data[0]['sprites']['front_default'])
filename = "pokemon_image.png"
r = requests.get(image, allow_redirects=True)
open(filename, 'wb').write(r.content)

pygame.init()

screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption('Pokemon')

white = (255, 255, 255)
black = (0, 0, 0)
font = pygame.font.Font('pokemon.ttf', 50)
text = font.render(name, True, black)
textRect = text.get_rect()
textRect.center = (250, 450)
img = pygame.image.load("pokemon_image.png").convert()
img = pygame.transform.scale(img, (500, 500))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(white)
    screen.blit(text, textRect)
    screen.blit(img, (0, 0))
    pygame.display.flip()
    