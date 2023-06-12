import pygame as py
import sys

py.init()
screen = py.display.set_mode([300,450])
py.display.set_caption('KnotZClickerHeroZ')
py.font.init()
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
purple = (127,0,255)
orange = (255,165,0)


background = 'black'
FPS = 60
font = py.font.SysFont('freesansbold.tiff', 20)
clock = py.time.Clock()

#game variables
green_val = 1
red_val = 2
orange_val = 3
white_val = 4
purple_val = 5
draw_green = False
draw_red = False
draw_orange = False
draw_white = False
draw_purple = False
green_len = 0
red_len = 0
orange_len = 0
white_len = 0
purple_len = 0
green_spd = 5
red_spd = 4
orange_spd = 3
white_spd = 2
purple_spd = 1
score = 0

#draw buttons
green_cost = 1
green_owned = False
green_manager_cost = 100
red_cost = 2
red_owned = False
red_manager_cost = 500
orange_cost = 3
orange_owned = False
orange_manager_cost = 1800
white_cost = 4
white_owned = False
white_manager_cost = 4800
purple_cost = 5
purple_owned = False
purple_manager_cost = 10000



def draw_task(color, y_cor, value, draw, length, speed):
    global score
    if draw and length < 200:
        length += speed
    elif length >= 200:
        draw = False
        length = 0
        score += value
    task = py.draw.circle(screen, color, (30, y_cor), 20, 5)
    py.draw.rect(screen, color, [70, y_cor -15, 200, 30])
    py.draw.rect(screen, 'black', [75,y_cor - 10, 190, 20])
    py.draw.rect(screen, color, [70, y_cor-15, length, 30])
    value_text = font.render(str(round(value, 2)), True, white)
    screen.blit(value_text, (27, y_cor - 8))

    return task, length, draw

def draw_buttons(color, x_cor, cost, owned, manager_cost):
    color_button = py.draw.rect(screen, color, [x_cor, 340, 50, 30])
    color_cost = font.render(str(round(cost, 2)), True, 'black')
    screen.blit(color_cost, (x_cor + 6, 350))
    if not owned:
        manager_button = py.draw.rect(screen, color, [x_cor, 405, 50, 30])
        manager_text = font.render(str(round(manager_cost, 2)), True, 'black')
        screen.blit(manager_text, (x_cor + 6, 410))
    else:
        manager_button = py.draw.rect(screen, 'black', [x_cor, 405, 50, 30])

    return color_button, manager_button


run = True
#main game loop
while run:
    clock.tick(FPS)

    for event in py.event.get():
        if event.type == py.QUIT:
            run = False

        if green_owned and not draw_green:
            draw_green = True
        if red_owned and not draw_red:
            draw_red = True
        if orange_owned and not draw_orange:
            draw_orange = True
        if white_owned and not draw_white:
            draw_white = True
        if purple_owned and not draw_purple:
            draw_purple = True
        if event.type == py.MOUSEBUTTONDOWN:
            if task1.collidepoint(event.pos):
                draw_green = True
            if task2.collidepoint(event.pos):
                draw_red = True
            if task3.collidepoint(event.pos):
                draw_orange = True
            if task4.collidepoint(event.pos):
                draw_white = True
            if task5.collidepoint(event.pos):
                draw_purple = True
            if green_manager_buy.collidepoint(event.pos) and score >= green_manager_cost and not green_owned:
                green_owned = True
                score -= green_manager_cost
            if red_manager_buy.collidepoint(event.pos) and score >= red_manager_cost and not red_owned:
                red_owned = True
                score -= red_manager_cost
            if orange_manager_buy.collidepoint(event.pos) and score >= orange_manager_cost and not orange_owned:
                orange_owned = True
                score -= orange_manager_cost
            if white_manager_buy.collidepoint(event.pos) and score >= white_manager_cost and not white_owned:
                white_owned = True
                score -= white_manager_cost
            if purple_manager_buy.collidepoint(event.pos) and score >= purple_manager_cost and not purple_owned:
                purple_owned = True
                score -= purple_manager_cost
            if green_buy.collidepoint(event.pos) and score >= green_cost:
                green_val += .15
                score -= green_cost
                green_cost += .1
            if red_buy.collidepoint(event.pos) and score >= red_cost:
                red_val += .3
                score -= red_cost
                red_cost += .2
            if orange_buy.collidepoint(event.pos) and score >= orange_cost:
                orange_val += .45
                score -= orange_cost
                orange_cost += .3
            if white_buy.collidepoint(event.pos) and score >= white_cost:
                white_val += .60
                score -= white_cost
                white_cost += .4
            if purple_buy.collidepoint(event.pos) and score >= purple_cost:
                purple_val += .75
                score -= purple_cost
                purple_cost += .5


    screen.fill(background)
    #draw clicker buttons on screen
    task1, green_len, draw_green = draw_task(green, 50, green_val, draw_green, green_len, green_spd)
    task2, red_len, draw_red = draw_task(red, 110, red_val, draw_red, red_len, red_spd)
    task3, orange_len, draw_orange = draw_task(orange, 170, orange_val, draw_orange, orange_len, orange_spd)
    task4, white_len, draw_white = draw_task(white, 230, white_val, draw_white, white_len, white_spd)
    task5, purple_len, draw_purple = draw_task(purple, 290, purple_val, draw_purple, purple_len, purple_spd)
    green_buy, green_manager_buy = draw_buttons(green, 10, green_cost, green_owned, green_manager_cost)
    red_buy, red_manager_buy = draw_buttons(red, 70, red_cost, red_owned, red_manager_cost)
    orange_buy, orange_manager_buy = draw_buttons(orange, 130, orange_cost, orange_owned, orange_manager_cost)
    white_buy, white_manager_buy = draw_buttons(white, 190, white_cost, white_owned, white_manager_cost)
    purple_buy, purple_manager_buy = draw_buttons(purple, 250, purple_cost, purple_owned, purple_manager_cost)

    display_score = font.render('Money: $'+str(round(score, 2)), True, white, 'black')
    screen.blit(display_score, (10,5))

    buy_more = font.render('Buy More:', True, white)
    screen.blit(buy_more, (10, 320))
    buy_managers = font.render('Buy Managers:', True, white)
    screen.blit(buy_managers, (10, 385))
    py.display.flip()

py.quit()