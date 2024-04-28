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

    pygame.font.init()
    screen = pygame.display.set_mode((640, 480))

    #screen = pygame.display.set_mode((width*scl, height*scl))
    pygame.display.set_caption("Game of Life")
    #
    clock = pygame.time.Clock()
    is_running = True
    # в начале программы ставим игру на паузу
    is_paused = True
    # переменной, в которой хранится шрифт
    main_font = pygame.font.Font(None, 24)
    while is_running:
        for event in pygame.event.get():
            # проверить закрытие окна
            if event.type == pygame.QUIT:
                is_running = False
            # если тип события - нажатая клавиша
            if event.type == pygame.KEYDOWN:
                # если эта клавиша - пробел
                if event.key == pygame.K_SPACE:
                    # Если была пауза, то снимем
                    if is_paused == True:
                        is_paused = False
                    # Если паузы не было, то ставим на паузу
                    else:
                        is_paused = True
            #  если нажата кнопка мыши
            if event.type == pygame.MOUSEBUTTONDOWN:
                # записываем позицию курстора в пикселях
                cursor_pos = event.pos
                # считаем индекс клетки по X
                x_pos = cursor_pos[0] // scl
                # считаем индекс клетки по Y
                y_pos = cursor_pos[1] // scl
                # создаем переменную, в которую пишем новое состояние
                # сначала пишем туда текущее состояние клетки, что не было ошибок,
                # если нажатие не будет обработано (например, нажата вторая кнопка мыши)\
                new_state = gof.field[y_pos][x_pos]
                # если нажата левая кнопка, то новое состояние - живая
                if event.button == 1:
                    new_state = 1
                # если нажата правая кнопка, то новое состояние - неживая
                elif event.button == 3:
                    new_state = 0
                # пишем в массив новое состояние клетки
                gof.field[y_pos][x_pos] = new_state
        # Если игра на паузе, то не обновляем состояние автомата, но рисовка
        # все равно должна быть
        if is_paused == False:
            gof.run_transition_rule()



        #gof.run_transition_rule()
        screen.fill((0, 0, 0))
        render_pygame(gof.field, screen, scl)
        text1 = main_font.render('Я люблю писать программы', True, (255, 255, 255))
        screen.blit(text1, (10, 450))

        pygame.display.flip()
        # держим цикл на правильной скорости
        clock.tick(60)
        pygame.time.delay(200)


if __name__ == '__main__':
    main()