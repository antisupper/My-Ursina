from ursina import *
import random
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# 1. Create the grid and water texture
grid = Entity(
    model=Grid(20, 20), scale=50, color=color.white, rotation_x=90, y=-1, collider='box'
)
water = Entity(
    model=Plane(subdivisions=(2, 8)), scale=50, color=color.white, texture='water.png', rotation_x=0, y=-0.5
)

# 2. Create boundaries
wall1 = Entity(model='cube', scale=(20, 12, 1), color=color.black, collider='box', x=0, z=-2)
wall2 = Entity(model='cube', scale=(20, 12, 1), color=color.black, collider='box', x=0, z=22)
wall3 = Entity(model='cube', scale=(24, 12, 1), color=color.black, collider='box', x=-10, z=10, rotation_y=90)
wall4 = Entity(model='cube', scale=(24, 12, 1), color=color.black, collider='box', x=10, z=10, rotation_y=90)

# 3. Create start and finish entities
start = Entity(model='cube', scale=(2, 1, 2), color=color.red, collider='box', x=0, z=0)
finish = Entity(model='cube', scale=(2, 1, 2), color=color.green, collider='box', x=0, z=20)

# 4. Create random blocks on the floor
cords = []
blocks = []
z = 0
x = 0

def generate_random_blocks():
    global blocks
    for block in blocks:
        destroy(block)
    blocks = []
    z = 0
    for i in range(6):
        z += 3
        for u in range(3):
            x = random.randrange(-8, 8, 3)
            bb = Entity(
                model='cube', scale=(2, 1, 2), color=color.orange, texture='stone.jpg', collider='box', x=x, z=z
            )
            blocks.append(bb)

generate_random_blocks()

# 5. Create the player in first person mode
fpc = FirstPersonController(model='cube', collider='box', position=(0.5, 1, 0.5))
fpc.cursor.visible = False

# 6. Update function to handle game logic
def update():
    hit_info = fpc.intersects()
    if hit_info.hit:
        if hit_info.entity in blocks:
            hit_info.entity.fade_out(duration=2)
            destroy(hit_info.entity, delay=2)
        # elif hit_info.entity == grid:
        #     end_game('YOU LOSE', reset=False)
        elif hit_info.entity == finish:
            end_game('YOU WON', reset=True)
            
    if held_keys["escape"]:
        application.quit()


# 7. Function to display end game message
def end_game(user_message, reset):
    message = Text(text=user_message, scale=0.25, origin=(0, 0), background=True, color=color.blue)
    invoke(destroy, message, delay=2)
    if reset:
        invoke(reset_game_state, delay=2)
    else:
        reset_game_state()
    
    application.resume()
    mouse.locked = True

# Function to reset the game state
def reset_game_state():
    generate_random_blocks()
    fpc.position = (0.5, 1, 0.5)

app.run()
