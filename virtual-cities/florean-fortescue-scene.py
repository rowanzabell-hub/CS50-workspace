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

    draw_ice_cream_shop(scene, 0, 0)

    scene.save_scene("florean-fortescue.html", "Florean Fortescue's Ice Cream Parlour HP")

def draw_ice_cream_shop(scene, cx, cz):
    #coral pink bottom floor
    scene.add_box(cx, 5, cz, 10, 10, 6, 255, 138, 118)
    # rasberry red middle floor
    scene.add_box(cx, 13, cz, 10, 6, 6, 217, 50, 81)
    # watermelon pink top floor
    scene.add_box(cx, 21, cz, 10, 10, 6, 243, 107, 130)

 


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
    scene.add_box(0, -25, 0, 1000, 50, 1000, 255, 255, 255)


main()

