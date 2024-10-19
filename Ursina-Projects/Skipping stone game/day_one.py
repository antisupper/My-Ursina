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
            
    if held_keys["escape"]:
        application.quit()




app.run()
