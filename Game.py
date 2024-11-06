import pygame
import random

# Константы
BLOCK_SIZE = 20
FPS = 10
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

# SRP: Класс для управления игрой
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.is_running = True

    def run(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.KEYDOWN:
                self.snake.change_direction(event.key)

    def update(self):
        self.snake.move()
        if self.snake.check_collision(self.food.position):
            self.snake.grow()
            self.food.respawn()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        pygame.display.flip()

# SRP: Класс для змейки
class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]
        self.direction = (BLOCK_SIZE, 0)

    def change_direction(self, key):
        if key == pygame.K_UP:
            self.direction = (0, -BLOCK_SIZE)
        elif key == pygame.K_DOWN:
            self.direction = (0, BLOCK_SIZE)
        elif key == pygame.K_LEFT:
            self.direction = (-BLOCK_SIZE, 0)
        elif key == pygame.K_RIGHT:
            self.direction = (BLOCK_SIZE, 0)

    def move(self):
        new_head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])

        # Проверка на выход за границы экрана
        if new_head[0] < 0 or new_head[0] >= SCREEN_WIDTH:
            self.direction = (-self.direction[0], self.direction[1])
        if new_head[1] < 0 or new_head[1] >= SCREEN_HEIGHT:
            self.direction = (self.direction[0], -self.direction[1])

        new_head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        self.body = [new_head] + self.body[:-1]

    def grow(self):
        self.body.append(self.body[-1])

    def check_collision(self, position):
        return self.body[0] == position

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))

# SRP: Класс для еды
class Food:
    def __init__(self):
        self.position = self.random_position()

    def random_position(self):
        x = random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        return x, y

    def respawn(self):
        self.position = self.random_position()

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE))

if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()