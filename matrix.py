from ursina import *

def update():
    for entity in cubes:
        entity.rotation_y += time.dt * 5
    global offset, offset2
    offset = offset + time.dt * 0.3
    offset2 = offset2 + time.dt * 0.4

    setattr(cube, "texture_offset", (0, offset))
    setattr(cube2, "texture_offset", (0, offset2))

app=Ursina()

cubes=[]
cube = Entity(model='cube', scale=(7,5,6), texture="img/geektech.png")
cubes.append(cube)
cube2 = Entity(model='cube', color=color.rgba(255,255,255,128), scale=(7.5,5,6.5),
               texture="img/naruto.png")

cubes.append(cube2)

offset = 0
offset2 = 0

app.run()