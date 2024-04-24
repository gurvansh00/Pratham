import pygame,pymunk
pygame.init()
display=pygame.display.set_mode ((600, 600))
clock=pygame.time.Clock()
space = pymunk.Space()
FPS = 50
class Ball():
  def

def game():
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    pygame.display.update()
    clock.tick(FPS)
    space.step(1/FPS)
game()
pygame.quit()
