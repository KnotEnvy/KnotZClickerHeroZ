import pygame as py


py.init()
screen = py.display.set_mode([300,450])
py.display.set_caption('KnotZClickerHeroZ')
py.font.init()
clock = py.time.Clock()

FPS = 60
font = py.font.SysFont('freesansbold.tiff', 20)

background = 'black'
score = 10000

class ColorTask:
    def __init__(self, color, value, y_cor, speed, cost, manager_cost, value_increment, manager_cost_increment):
        self.color = color
        self.value = value
        self.y_cor = y_cor
        self.speed = speed
        self.draw = False
        self.length = 0
        self.cost = cost
        self.manager_cost = manager_cost
        self.owned = False
        self.value_increment = value_increment
        self.cost_increment = manager_cost_increment

    def draw_task(self):
        global score
        if self.draw and self.length < 200:
            self.length += self.speed
        elif self.length >= 200:
            self.draw = False
            self.length = 0
            score += self.value
        task = py.draw.circle(screen, self.color, (30, self.y_cor), 20, 5)
        py.draw.rect(screen, self.color, [70, self.y_cor -15, 200, 30])
        py.draw.rect(screen, 'black', [75,self.y_cor - 10, 190, 20])
        py.draw.rect(screen, self.color, [70, self.y_cor-15, self.length, 30])
        value_text = font.render(str(round(self.value, 2)), True, 'white')
        screen.blit(value_text, (27, self.y_cor - 8))

        return task

    def draw_buttons(self, x_cor):
        color_button = py.draw.rect(screen, self.color, [x_cor, 340, 50, 30])
        color_cost = font.render(str(round(self.cost, 2)), True, 'black')
        screen.blit(color_cost, (x_cor + 6, 350))
        if not self.owned:
            manager_button = py.draw.rect(screen, self.color, [x_cor, 405, 50, 30])
            manager_text = font.render(str(round(self.manager_cost, 2)), True, 'black')
            screen.blit(manager_text, (x_cor + 6, 410))
        else:
            manager_button = py.draw.rect(screen, 'black', [x_cor, 405, 50, 30])

        return color_button, manager_button

## order of attributes for tasks
## color, value, y loation, speed, cost, manager_cost, value_increment, cost_increment
color_tasks = [
    ColorTask((0,255,0), 1, 50, 5, 1, 100, 0.25, 0.25),
    ColorTask((255,0,0), 2, 110, 4, 2, 500, 1, 1),
    ColorTask((255,165,0), 3, 170, 3, 3, 1800, 3, 1.5),
    ColorTask((255,255,255), 4, 230, 2, 4, 4800, 5, 3),
    ColorTask((127,0,255), 5, 290, 1, 5, 10000, 25, 10)
]

run = True
#main game loop
while run:
    clock.tick(FPS)

    for event in py.event.get():
        if event.type == py.QUIT:
            run = False

        if event.type == py.MOUSEBUTTONDOWN:
            for i, task in enumerate(color_tasks):
                if task.draw_buttons(10 + i * 60)[0].collidepoint(event.pos) and score >= task.cost:
                    task.value += task.value_increment
                    score -= task.cost
                    task.cost += task.cost_increment
                if task.draw_buttons(10 + i * 60)[1].collidepoint(event.pos) and score >= task.manager_cost and not task.owned:
                    task.owned = True
                    score -= task.manager_cost
                if task.draw_task().collidepoint(event.pos):
                    task.draw = True
    for task in color_tasks:
        if task.owned and not task.draw:
            task.draw = True

    screen.fill(background)

    for i, task in enumerate(color_tasks):
        task.draw_task()
        task.draw_buttons(10 + i * 60)

    display_score = font.render('Money: $'+str(round(score, 2)), True, 'white', 'black')
    screen.blit(display_score, (10,5))

    buy_more = font.render('Buy More:', True, 'white')
    screen.blit(buy_more, (10, 320))
    buy_managers = font.render('Buy Managers:', True, 'white')
    screen.blit(buy_managers, (10, 385))
    py.display.flip()

py.quit()