from ursina import*
import random

app = Ursina()
window.size = window.fullscreen_size
window.position = Vec2(0, 0)
window.color = color.white

# ball_colors = [color.red, color.blue, color.green, color.yellow, color.white]
# ball_color = random.choice(ball_colors)
# print(ball_color)

upper = Entity(model = 'quad', x = 0, y = 4, scale = (16,0.2), collider = 'box', color = color.black)
left = Entity(model = 'quad', x = -7.2, y = 0, scale = (0.2, 10), collider = 'box', color = color.black)
right = Entity(model = 'quad', x = 7.2, y = 0, scale = (0.2, 10), collider = 'box', color = color.black)
ball = Entity(model = 'circle', scale = 0.2, collider = 'box', dx = 0.05, dy = 0.03, color = color.random_color())
paddle = Entity(model = 'quad', x = 0, y = -3.5, scale = (2, 0.2),  collider='box', color = color.black)

bricks = []
for x_pos in range(-65, 75, 10):
    for y_pos in range(6,10):
        brick = Entity(model='quad', x = x_pos/10 , y = y_pos/3, scale = (0.9, 0.3),  collider='box', color = color.red)
        bricks.append(brick)
count = 0
p_speed = 8
b_speed = 9
def update():
    global count
    ball.x += ball.dx
    ball.y += ball.dy
    paddle.x += (held_keys['right arrow'] - held_keys['left arrow']) * time.dt *5 or (held_keys['d'] - held_keys['a']) * time.dt *5 
    hit_info = ball.intersects()
    if hit_info.hit:        
        if hit_info.entity == left or hit_info.entity == right:
            ball.dx = -ball.dx
        if hit_info.entity == upper:
            ball.dy = -ball.dy
        if hit_info.entity in bricks:
            destroy(hit_info.entity)
            bricks.remove(hit_info.entity)
            ball.dy = -ball.dy
            count += 1
            print(count)
        if hit_info.entity == paddle:
            ball.dy = -ball.dy
            ball.dx = 0.05*(ball.x - paddle.x)
            ball.color = color.random_color()
    if ball.y < -5:
        message = Text(text = 'You LOST, your score' + str(count), scale=2, origin=(0,0), background=True, color=color.blue)
        application.pause()
    if len(bricks) == 0:
        message = Text(text = 'You WON', scale=2, origin=(0,0), background=True, color=color.blue)
        application.pause()

ball.update = update

app.run()

