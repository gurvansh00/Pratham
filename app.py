import pygame,pymunk
import streamlit as st
st.title('Experiment')
pygame.init()
col1,col2 = st.columns([0.7,0.3])
with col2:
  st.slider('Length',1,10)

with col1:
  display=pygame.display.set_mode ((600, 600))
  clock=pygame.time.Clock()
  space = pymunk.Space()
  FPS = 50
  def convert_coordinates(point):
    return int(point[0]), int(600-point[1])
  class Ball():
    def init_(self, x, y):
      self.body = pymunk.Body()
      self.body. position = x, y
      self.shape = pymunk.Circle（self.body, 10）
      self.shape.density = 1
      self.shape.elasticity = 1
    def draw(self):
      pygame.draw.circle(display, (255,0,0), convert_coordinates(self.body.position),10

  
  def game():
    ball_1 = Ball(300,300)
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          return
      display.fill((255,255,255))
      ball_1.draw()
      pygame.display.update()
      clock.tick(FPS)
      space.step(1/FPS)
  game()
  pygame.quit()


