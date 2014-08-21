import pyglet

window = pyglet.window.Window(style=pyglet.window.Window.WINDOW_STYLE_DIALOG, fullscreen=True)
image = pyglet.resource.image('kitten.png')

@window.event
def on_draw():
  window.clear()
  image.blit(0, 0)

if __name__ == "__main__":
  pyglet.app.run()