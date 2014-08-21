import pyglet
from pyglet.window import key, mouse

window = pyglet.window.Window(width=800, height=600)

class MyKitten():
  x = y = 0
  image = pyglet.resource.image('kitten.png')

myKitten = MyKitten()

@window.event
def on_key_press(symbol, modifiers):
  if symbol == key.A:
    print 'The "A" key was pressed.'
  elif symbol == key.LEFT:
    print "The left arrow key was pressed."
  elif symbol == key.ENTER:
    print "The enter key was pressed"

@window.event
def on_mouse_drag(x, y, dx, dy, button, modifiers):
  if button == mouse.LEFT:
    myKitten.x = x
    myKitten.y = y

@window.event
def on_draw():
  window.clear()
  myKitten.image.blit(myKitten.x, myKitten.y)

if __name__ == '__main__':
  pyglet.app.run()