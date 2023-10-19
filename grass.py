from pico2d import load_image


class Grass:
    def __init__(self, x = 400, y = 30, velocity = 1):
        self.image = load_image('grass.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass
