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

# 4. Create the grid to track block positions
grid_size = 20
grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
blocks = []

def generate_random_blocks():
    global blocks, grid
    for block in blocks:
        destroy(block)
    blocks = []
    
    # Create a clear path from start to finish
    for z in range(1, grid_size):
        grid[z][10] = 1  # Mark the path on the grid

    # Function to check if a position is valid (within bounds and not occupied)
    def is_valid_position(x, z):
        return 0 <= x < grid_size and 0 <= z < grid_size and grid[z][x] == 0

    # Place blocks around the path
    for z in range(1, grid_size - 1, 3):
        for _ in range(3):  # 3 blocks per row
            while True:
                x = random.choice(range(1, grid_size, 3))
                if is_valid_position(x, z):
                    grid[z][x] = 1
                    break
            block = Entity(
                model='cube', scale=(2, 1, 2), color=color.orange, texture='stone.jpg', collider='box', x=x - 10, z=z
            )
            blocks.append(block)

generate_random_blocks()

# 5. Create the player in first person mode
fpc = FirstPersonController(model='cube', collider='box', position=(0.5, 1, 0.5))
fpc.cursor.visible = False


def update():         
    if held_keys["escape"]:
        application.quit()




app.run()
