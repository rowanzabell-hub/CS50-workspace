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

    # TODO (Task 1): call draw_tree to plant a tree. Remember to pass scene first!
    draw_tree(scene,-3, -8, 8)
    draw_tree(scene,-2, -9, 10)
    draw_fire_hydrant(scene, 2, -8)
    add_meshes(scene)
    # Draw two city blocks
    draw_city_block(scene, 0, -25)
    draw_city_block(scene, 30, -25)
    scene.save_scene("simplescene.html", "Simple Sample Scene")
    draw_sedan(scene, 4, 2, 255, 0, 0, ry=90)

def draw_tree(scene, cx, cz, height):
    scene.add_cylinder(cx, height / 4, cz, height / 8, height / 2, 102, 51, 0)
    scene.add_ellipsoid(cx, height * 3 / 4, cz, height / 3, height / 4, height / 3, 0, 255, 0)



# Task 2 and beyond: define your own functions!


def draw_fire_hydrant(scene, cx, cz):
    scene.add_cylinder(cx, 0.15, cz, 0.35, 0.3, 255, 0, 0)
    scene.add_cylinder(cx, 0.55, cz, 0.25, 0.6, 255, 0, 0)
    scene.add_sphere(cx, 0.85, cz, 0.2, 255, 0, 0)
    scene.add_box(cx - 0.35, 0.65, cz, 0.3, 0.2, 0.2, 255, 0, 0)
    scene.add_box(cx + 0.35, 0.65, cz, 0.3, 0.2, 0.2, 255, 0, 0)


def draw_stop_light(scene, cx, cz):
    # Vertical pole
    scene.add_cylinder(cx, 4, cz, 0.15, 8, 100, 100, 100)

    # Horizontal pole
    scene.add_box(cx + 4, 8, cz, 8, 0.2, 0.2, 100, 100, 100)

    # Black traffic light housing
    scene.add_box(cx + 7, 7, cz, 1, 2.5, 0.7, 30, 30, 30)

    # Red light
    scene.add_sphere(cx + 7, 7.8, cz + 0.4, 0.3, 255, 0, 0)

    # Yellow light
    scene.add_sphere(cx + 7, 7, cz + 0.4, 0.3, 255, 255, 0)

    # Green light
    scene.add_sphere(cx + 7, 6.2, cz + 0.4, 0.3, 0, 255, 0)

def draw_sedan(scene, cx, cz, r, g, b, ry=0):
    group = scene.add_group(cx,0, cz, 0, ry, 0)

    # Car body
    group.add_box(0, 0.85, 0, 4.5, 0.7, 1.7, r, g, b)

    # Car cabin
    group.add_box(-0.3, 1.55, 0, 3.5, 0.8, 1.4, r, g, b)
    group.add_cylinder(-)



def draw_city_block(scene, cx, cz):
    # Building
    scene.add_box(cx, 6, cz - 15, 10, 12, 8, 180, 190, 220)

    # Two trees with different heights
    draw_tree(scene, cx - 8, cz - 8, 6)
    draw_tree(scene, cx + 8, cz - 8, 9)

    # Fire hydrant
    draw_fire_hydrant(scene, cx - 5, cz - 3)

    # Traffic light
    draw_stop_light(scene, cx - 12, cz - 5)

    # Two cars
    draw_sedan(scene, cx - 4, cz + 4, 255, 50, 50)
    draw_sedan(scene, cx + 5, cz + 4, 50, 100, 255, 90)

    group.add_cylinder(cx, height/2, 0, 0.3, height, 128,128,128)
    group.add_cylinder(cx, height/2, 0, 0.3, height, 128,128,128)



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

