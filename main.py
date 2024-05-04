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


def render_pygame(field, scr, scale, color):
    # scale = 15
    for y in range(0, len(field)):
        for x in range(0, len(field[0])):
            if field[y][x] == 0:
                pygame.draw.rect(scr, (255, 255, 255), (x * scale, y * scale, scale, scale))
            elif field[y][x] == 1:
                pygame.draw.rect(scr, color, (x * scale, y * scale, scale, scale))
            # рисуем обводку
            pygame.draw.rect(scr, (0, 0, 0), (x * scale, y * scale, scale, scale), 2)


def main():
    width = int(input('Введите ширину поля: '))
    height = int(input('Введите высоту поля: '))
    life_count = int(input('Введите процент живых клеток: '))
    if life_count >= 90:
        print('Слишком много живых клеток')
        life_count = int(input('Введите процент живых клеток: '))
    scl = int(input('Введите масштаб отрисовки: '))
    if width * scl >= 640:
        print('Поле не поместится на экране. Выберите меньший масштаб')
        scl = int(input('Введите масштаб отрисовки: '))
    print(
        'Выберите тип автомата: 0 - по умолчанию; 1 - умирает, когда 0 или больше 5; 2 - оживает от 2 до 4 включительно')
    type = int(input())

    # r g b
    clr = (0, 0, 255)

    # height = width
    if type == 1:
        gof = GameOfLifeHeirOne(width, height)
    elif type == 2:
        gof = GameOfLifeHeirTwo(width, height)
    elif type == 0:
        gof = GameOfLife(width, height)
    else:
        print('Неверный тип')
        print(
            'Выберите тип автомата: 0 - по умолчанию; 1 - умирает, когда 0 или больше 5; 2 - оживает от 2 до 4 включительно')
        type = int(input())
    gof.initialize(life_count)
    pygame.init()

    pygame.font.init()
    # screen = pygame.display.set_mode((640, 480))

    screen = pygame.display.set_mode((width * scl + 250, height * scl))
    pygame.display.set_caption("Game of Life")
    #
    clock = pygame.time.Clock()
    is_running = True
    # в начале программы ставим игру на паузу
    is_paused = True
    # переменной, в которой хранится шрифт
    main_font = pygame.font.Font(None, 24)
    count_iter = 1
    while is_running:
        for event in pygame.event.get():
            # проверить закрытие окна
            if event.type == pygame.QUIT:
                is_running = False
            # если тип события - нажатая клавиша
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    is_running = False
                # если эта клавиша - пробел
                if event.key == pygame.K_SPACE:
                    # Если была пауза, то снимем
                    if is_paused == True:
                        is_paused = False
                    # Если паузы не было, то ставим на паузу
                    else:
                        is_paused = True
                #                    gof.run_transition_rule()
                #                    count_iter += 1
                # по кнопке вниз один шаг
                if event.key == pygame.K_DOWN:
                    gof.run_transition_rule()
                    count_iter += 1
                # по стрелке вправо меняется цвет синий-красный-зеленый
                if event.key == pygame.K_RIGHT:
                    if clr == (255, 0, 0):
                        clr = (0, 255, 0)
                    elif clr == (0, 255, 0):
                        clr = (0, 0, 255)
                    else:
                        clr = (255, 0, 0)
                # по кнопке R рестарт к стартовым настройкам
                if event.key == pygame.K_r:
                    gof.reinit()
                    gof.initialize(life_count)
                    count_iter = 1

            #  если нажата кнопка мыши
            if event.type == pygame.MOUSEBUTTONDOWN:
                # записываем позицию курсора в пикселях
                cursor_pos = event.pos
                # считаем индекс клетки по X
                x_pos = cursor_pos[0] // scl
                # считаем индекс клетки по Y
                y_pos = cursor_pos[1] // scl

                # создаем переменную, в которую пишем новое состояние
                # сначала пишем туда текущее состояние клетки, что не было ошибок,
                # если нажатие не будет обработано (например, нажата вторая кнопка мыши)
                try:
                    new_state = gof.field[y_pos][x_pos]
                    # если нажата левая кнопка, то новое состояние - живая
                    if event.button == 1:
                        new_state = 1
                    # если нажата правая кнопка, то новое состояние - неживая
                    elif event.button == 3:
                        new_state = 0
                    # пишем в массив новое состояние клетки
                    gof.field[y_pos][x_pos] = new_state
                except:
                    print('Ошибка! Точка за пределами поля')

        # Если игра на паузе, то не обновляем состояние автомата, но рисовка
        # все равно должна быть
        if is_paused == False:
            gof.run_transition_rule()
            count_iter += 1
        count_life = 0
        for y in range(0, len(gof.field)):
            for x in range(0, len(gof.field[0])):
                if gof.field[y][x] == 1:
                    count_life += 1

        screen.fill((100, 100, 100))

        render_pygame(gof.field, screen, scl, clr)
        text1 = main_font.render(f'размер поля: {width * scl} x {height * scl}', True, (0, 0, 0))
        screen.blit(text1, (width * scl + 5, 5))
        text2 = main_font.render(f'кол-во живых клеток: {count_life}', True, (0, 0, 0))
        screen.blit(text2, (width * scl + 5, 25))
        text3 = main_font.render(f'кол-во мертвых клеток: {width * height - count_life}', True, (0, 0, 0))
        screen.blit(text3, (width * scl + 5, 45))
        text4 = main_font.render(f'размер квадрата: {scl} x {scl}', True, (0, 0, 0))
        screen.blit(text4, (width * scl + 5, 65))
        text5 = main_font.render(f'цвет живых клеток', True, clr)
        screen.blit(text5, (width * scl + 5, 85))
        text6 = main_font.render(f'цвет мертвых клеток', True, (255, 255, 255))
        screen.blit(text6, (width * scl + 5, 105))
        text7 = main_font.render(f'кол-во итераций: {count_iter}', True, (0, 0, 0))
        screen.blit(text7, (width * scl + 5, 125))
        pygame.display.flip()
        # gof.run_transition_rule()
        # держим цикл на правильной скорости
        clock.tick(60)
        pygame.time.delay(200)


if __name__ == '__main__':
    main()