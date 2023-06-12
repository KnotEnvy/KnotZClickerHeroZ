import pygame as py

py.init()
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 450
screen = py.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), py.RESIZABLE)
py.display.set_caption('KnotZClickerHeroZ')
py.font.init()
clock = py.time.Clock()

FPS = 60
font = py.font.SysFont('freesansbold.tiff', 20)

background = 'black'
score = 10000

class ColorTask:
    def __init__(self, color, value, y_percent, speed, cost, manager_cost, value_increment, manager_cost_increment):
        self.color = color
        self.value = value
        self.y_percent = y_percent
        self.speed = speed
        self.draw = False
        self.length = 0
        self.cost = cost
        self.manager_cost = manager_cost
        self.owned = False
        self.value_increment = value_increment
        self.cost_increment = manager_cost_increment

    def draw_task(self):
        global score, WINDOW_WIDTH, WINDOW_HEIGHT
        y_cor = int(WINDOW_HEIGHT * self.y_percent)
        if self.draw and self.length < int(WINDOW_WIDTH *.65):
            self.length += self.speed
        elif self.length >= int(WINDOW_WIDTH *.65):
            self.draw = False
            self.length = 0
            score += self.value
        task = py.draw.circle(screen, self.color, (int(WINDOW_WIDTH * 0.1), y_cor), int(WINDOW_HEIGHT * 0.04), 5)
        py.draw.rect(screen, self.color, [int(WINDOW_WIDTH * 0.23), y_cor - int(WINDOW_HEIGHT * 0.033), int(WINDOW_WIDTH * 0.67), int(WINDOW_HEIGHT * 0.067)])
        py.draw.rect(screen, 'black', [int(WINDOW_WIDTH * 0.25), y_cor - int(WINDOW_HEIGHT * 0.022), int(WINDOW_WIDTH * 0.63), int(WINDOW_HEIGHT * 0.044)])
        py.draw.rect(screen, self.color, [int(WINDOW_WIDTH * 0.23), y_cor - int(WINDOW_HEIGHT * 0.033), self.length, int(WINDOW_HEIGHT * 0.067)])
        value_text = font.render(str(round(self.value, 2)), True, 'white')
        screen.blit(value_text, (int(WINDOW_WIDTH * 0.09), y_cor - int(WINDOW_HEIGHT * 0.018)))

        return task

    def draw_buttons(self, x_percent):
        global score, WINDOW_WIDTH, WINDOW_HEIGHT
        x_cor = int(WINDOW_WIDTH * x_percent)
        color_button = py.draw.rect(screen, self.color, [x_cor, int(WINDOW_HEIGHT * 0.756), int(WINDOW_WIDTH * 0.167), int(WINDOW_HEIGHT * 0.067)])
        color_cost = font.render(str(round(self.cost, 2)), True, 'black')
        screen.blit(color_cost, (x_cor + int(WINDOW_WIDTH * 0.02), int(WINDOW_HEIGHT * 0.78)))
        if not self.owned:
            manager_button = py.draw.rect(screen, self.color, [x_cor, int(WINDOW_HEIGHT * 0.9), int(WINDOW_WIDTH * 0.167), int(WINDOW_HEIGHT * 0.067)])
            manager_text = font.render(str(round(self.manager_cost, 2)), True, 'black')
            screen.blit(manager_text, (x_cor + int(WINDOW_WIDTH * 0.02), int(WINDOW_HEIGHT * 0.92)))
        else:
            manager_button = py.draw.rect(screen, 'black', [x_cor, int(WINDOW_HEIGHT * 0.9), int(WINDOW_WIDTH * 0.167), int(WINDOW_HEIGHT * 0.067)])

        return color_button, manager_button

## order of attributes for tasks
## color, value, y loation, speed, cost, manager_cost, value_increment, cost_increment
color_tasks = [
    ColorTask((0,255,0), 1, 0.11, WINDOW_WIDTH * 0.01, 1, 100, 0.25, 0.25),
    ColorTask((255,0,0), 2, 0.24, WINDOW_WIDTH * 0.008, 2, 500, 1, 1),
    ColorTask((255,165,0), 3, 0.37, WINDOW_WIDTH * 0.006, 3, 1800, 3, 1.5),
    ColorTask((255,255,255), 4, 0.50, WINDOW_WIDTH * 0.004, 4, 4800, 5, 3),
    ColorTask((127,0,255), 5, 0.63, WINDOW_WIDTH * 0.002, 5, 10000, 25, 10)
]


run = True
#main game loop
while run:
    clock.tick(FPS)

    for event in py.event.get():
        if event.type == py.QUIT:
            run = False

        if event.type == py.VIDEORESIZE:
            WINDOW_WIDTH, WINDOW_HEIGHT = event.w, event.h
            screen = py.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), py.RESIZABLE)

        if event.type == py.MOUSEBUTTONDOWN:
            for i, task in enumerate(color_tasks):
                if task.draw_buttons(0.02 + i * 0.13)[0].collidepoint(event.pos) and score >= task.cost:
                    task.value += task.value_increment
                    score -= task.cost
                    task.cost += task.cost_increment
                if task.draw_buttons(0.02 + i * 0.13)[1].collidepoint(event.pos) and score >= task.manager_cost and not task.owned:
                    task.owned = True
                    score -= task.manager_cost
                if task.draw_task().collidepoint(event.pos):
                    task.draw = True
    for task in color_tasks:
        if task.owned and not task.draw:
            task.speed = WINDOW_WIDTH * task.speed / WINDOW_WIDTH
            task.draw = True

    screen.fill(background)

    for i, task in enumerate(color_tasks):
        task.draw_task()
        task.draw_buttons(0.02 + i * 0.13)

    display_score = font.render('Money: $'+str(round(score, 2)), True, 'white', 'black')
    screen.blit(display_score, (int(WINDOW_WIDTH * 0.02), int(WINDOW_HEIGHT * 0.01)))

    buy_more = font.render('Buy More:', True, 'white')
    screen.blit(buy_more, (int(WINDOW_WIDTH * 0.02), int(WINDOW_HEIGHT * 0.71)))
    buy_managers = font.render('Buy Managers:', True, 'white')
    screen.blit(buy_managers, (int(WINDOW_WIDTH * 0.02), int(WINDOW_HEIGHT * 0.85)))
    py.display.flip()

py.quit()

