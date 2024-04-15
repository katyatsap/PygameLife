from cellular_automata import *
import pygame

def render_field(field):
    for y in range(0, len(field)):
        for x in range(0, len(field[0])):
            if field[y][x] == 0:
                print(' ', end='')
            elif field[y][x] == 1:
                print('X', end='')
        print()
    print('----------------------')

def render_pygame(field, scr):
    scale = 15
    for y in range(0, len(field)):
        for x in range(0, len(field[0])):
            if field[y][x] == 0:
                pygame.draw.rect(scr, (255, 255, 255), (x * scale, y * scale, scale, scale))
            elif field[y][x] == 1:
                pygame.draw.rect(scr, (0, 0, 255), (x * scale, y * scale, scale, scale))
            # рисуем обводку
            pygame.draw.rect(scr, (0, 0, 0), (x * scale, y * scale, scale, scale), 2)


def main():
    gof = GameOfLife(30, 30)
    gof.initialize(30)

    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Game of Life")
    clock = pygame.time.Clock()
    is_running = True
    while is_running:
        for event in pygame.event.get():
            # проверить закрытие окна
            if event.type == pygame.QUIT:
                is_running = False
        gof.run_transition_rule()
        screen.fill((0, 0, 0))
        render_pygame(gof.field, screen)
        pygame.display.flip()
        # держим цикл на правильной скорости
        clock.tick(60)
        pygame.time.delay(200)



if __name__ == '__main__':
    main()