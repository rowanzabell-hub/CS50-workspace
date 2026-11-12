"""
Virtual Cities!

Instructions and Documentation:
https://gist.github.com/mrsharp-milken/21c48a631c51849a83bf6f05ea9c8b86
"""

from Scene3D import Scene3D

def main():
    scene = Scene3D()

    setup_lights(scene)
    setup_cameras(scene)
    add_ground(scene)

    # Draw three snowmen in different places
    simple_snowman(scene, -4, -8)
    simple_snowman(scene, 0, -12)
    simple_snowman(scene, 5, -6)

    # TODO (Task 1): call tulip() to plant a tulip. Remember to pass scene first!
    tulip(scene, 1, 3, 1)
    tulip(scene, 2, 4, 2)
    tulip(scene, 3, 4, 5)
    draw_sedan(scene, 10, 5, 255, 0, 0)
    streetlight(scene, 8, 4)
    traffic_cone(scene, 6, 4)

    draw_city_block(scene, 0, 0)
    draw_city_block(scene, 30, 0)
    add_meshes(scene)

    scene.save_scene("simplescene.html", "Simple Sample Scene")


def tulip(scene, cx, cz, height):
    #add_cylinder(cx, cy, cz, radius, height, r, g, b)
    scene.add_cylinder(cx, height/2, cz, .1, height, 150, 234, 133)
    scene.add_cone(cx, height, cz, .25, .6,255, 0, 0, rz=180)
# Task 2 and beyond: define your own functions!

def traffic_cone(scene, cx, cz):
    #add_box(cx, cy, width, height, depth, r, g, b)
    scene.add_box(cx, 0.1, cz, 0.8, 0.2, 0.8, 255, 80, 0)
    #add_cone(cx, cy, cz, radius, height, r, g, b)
    scene.add_cone(cx, 0.7, cz, 0.3, 1, 255, 80, 0)
    scene.add_cylinder(cx, 0.6, cz, 0.22, 0.12, 255, 255, 255)

def streetlight(scene, cx, cz):
    group = scene.add_group(cx, 0, cz, 0, 0, 0)
    #add_cylinder(cx, cy, cz, radius, height, r, g, b,)
    scene.add_cylinder(cx, 2, cz, 0.15, 4, 100, 100, 100)
    #add_box(cx, cy, cz, width, height, depth, r, g, b)
    group.add_box(2.7, 3.95, 0, 0.7, 0.25, 0.5, 255, 255, 180)
    scene.add_box( cx, 0.15, cz, 0.7, 0.3, 0.7, 100, 100, 100)
    group.add_box(1.5, 4.2, 0, 3, 0.2, 0.2, 80, 80, 80)
    group.add_box(2.7, 4.1, 0, 0.9, 0.15, 0.6, 80, 80, 80)
def draw_sedan(scene, cx, cz, r, g, b, ry=0):
    group = scene.add_group(cx,0, cz, 0, ry, 0)

    # Car body
    group.add_box(0, 0.85, 0, 4.5, 0.7, 1.7, r, g, b)

    # Car cabin
    group.add_box(-0.3, 1.55, 0, 3.5, 0.8, 1.4, r, g, b)
    group.add_cylinder(-1.8, 0.5, 0.9, 0.5,  0.25, 127, 127, 127, rx=90)
    group.add_cylinder(1.8, 0.5, 0.9, 0.5, 0.25, 127, 127, 127, rx=90)
    group.add_cylinder(-1.8, 0.5, -0.9, 0.5, 0.25, 127, 127, 127, rx=90)
    group.add_cylinder(1.8, 0.5, -0.9, 0.5, 0.25, 127, 127, 127, rx=90)
def draw_city_block(scene, cx, cz):
    # Building
    scene.add_box(cx, 6, cz - 15, 10, 12, 8, 180, 190, 220)
    

     # Two tulips with different heights
    group= scene.add_group(cx, 0, cz, 0, 0, 0)
    tulip(scene, cx, cz, 1)
    tulip(group, 2, 0, 2)
    tulip(group, 5, 0, 5)

    # traffic cone
    traffic_cone(group, 5, 0)
    # Street light
    streetlight(group, 8, 0)

    # Two cars
    draw_sedan(scene, cx - 4, cz + 4, 255, 50, 50)
    draw_sedan(scene, cx + 5, cz + 4, 50, 100, 255, 90)

    # building (make box)





# All functions need "scene" as the first parameter
# cx and cz say where the snowman's center goes
def simple_snowman(scene, cx, cz):
    # Big white bottom ball (radius 1, so its center is 1 above the ground)
    scene.add_sphere(cx, 1, cz, 1, 255, 255, 255)
    # Smaller white ball on top (radius 0.7), resting on the bottom ball
    scene.add_sphere(cx, 2.5, cz, 0.7, 255, 255, 255)
    # Black box for a hat, sitting on top of the head
    scene.add_box(cx, 3.4, cz, 0.7, 0.4, 0.7, 0, 0, 0)


def setup_lights(scene):
    scene.add_point_light(-100, 200, 0, 200, 200, 200, 1.0)
    scene.add_point_light(100, 200, 0, 200, 200, 200, 1.0)
    scene.add_point_light(0, 0, -100, 200, 200, 200, 1.0)
    scene.add_point_light(0, 0, 100, 200, 200, 200, 1.0)

def setup_cameras(scene):
    scene.add_camera(0, 2, 0, 0)
    scene.add_camera(0, 2, -40, 180)

def add_ground(scene):
    # Add a large gray box for the ground
    scene.add_box(0, -25, 0, 1000, 50, 1000, 100, 100, 100)

def add_meshes(scene):
    scene.add_mesh("meshes/cow.obj", 1, 1, -7, 0, 0, 0, 1, 1, 1, 0, 255, 255)
    scene.add_textured_mesh("meshes/smokestack/medres.obj", "meshes/smokestack/medres.mtl",
                            0, 18, -20, 0, 180, 0, 10, 10, 10, 0)

main()

