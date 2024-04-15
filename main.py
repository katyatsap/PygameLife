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

def render_pygame(field, scr, scale):
    #scale = 15
    for y in range(0, len(field)):
        for x in range(0, len(field[0])):
            if field[y][x] == 0:
                pygame.draw.rect(scr, (255, 255, 255), (x*scale, y*scale, scale, scale))
            elif field[y][x] == 1:
                pygame.draw.rect(scr, (0, 0, 255), (x*scale, y*scale, scale, scale))
            # рисуем обводку
            pygame.draw.rect(scr, (0, 0, 0), (x * scale, y * scale, scale, scale), 2)


def main():
    width = int(input('Введите ширину поля: '))
    height = int(input('Введите высоту поля: '))
    life_count = int(input('Введите изначальное количество живых клеток: '))
    if life_count >= width*height - ((width-1)*2+height*2):
        print('Слишком много живых клеток')
        life_count = int(input('Введите изначальное количество живых клеток: '))
    scl = int(input('Введите масштаб отрисовки: '))
    if width*scl >=640:
        print('Поле не поместится на экране. Выберите меньший масштаб')
        scl = int(input('Введите масштаб отрисовки: '))
    print('Выберите тип автомата: 0 - по умолчанию; 1 - умирает, когда 0 или больше 5; 2 - оживает от 2 до 4 включительно')
    type = int(input())
    #height = width
    if type == 1:
        gof = GameOfLifeHeirOne(width, height)
    elif type == 2:
        gof = GameOfLifeHeirTwo(width, height)
    elif type == 0:
        gof = GameOfLife(width, height)
    else:
        print('Неверный тип')
        print('Выберите тип автомата: 0 - по умолчанию; 1 - умирает, когда 0 или больше 5; 2 - оживает от 2 до 4 включительно')
        type = int(input())
    gof.initialize(life_count)
    pygame.init()
    screen = pygame.display.set_mode((width*scl, height*scl))
    pygame.display.set_caption("Game of Life")
    clock = pygame.time.Clock()
    is_running = True
    while is_running:
        for event in pygame.event.get():
            # проверить закрытие окна
            if  event.type == pygame.QUIT:
                is_running = False
        gof.run_transition_rule()
        screen.fill((0, 0, 0))
        render_pygame(gof.field, screen, scl)
        pygame.display.flip()
        # держим цикл на правильной скорости
        clock.tick(60)
        pygame.time.delay(200)


if __name__ == '__main__':
    main()
