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

    #fancy gold
    scene.add_box(cx, 10, 3.1, 10.3, 0.25, 0.4, 255, 200, 70)
    scene.add_box(cx, 16, 3.1, 10.3, 0.25, 0.4, 255, 200, 70)
    scene.add_box(cx, 26, 3.1, 10.3, 0.25, 0.4, 255, 200, 70)

    #new windows
    draw_display_window(scene, -3)
    draw_display_window(scene, 3)
    draw_fairytail_window(scene, -3.4)
    draw_fairytail_window(scene, 3.4)
    draw_rainbow_window(scene, 0)

def draw_display_window(scene, cx):
    # gold frame
    scene.add_box(cx, 5, 3.2, 2.5, 7.2, 0.2, 255, 200, 70)
    #clear mint class
    scene.add_box(cx, 5, 3.4, 2.2, 6.9, 0.1, 183, 228, 176, opacity=0.4)
    # gold div
    scene.add_box(cx, 5, 3.5, 0.08, 6.9, 0.1, 255, 200, 70)
    # gold mid
    scene.add_box(cx, 5, 3.5, 2.2, 0.08, 0.1, 255, 200, 70)
    # gold low
    scene.add_box(cx, 3, 3.5, 2.2, 0.08, 0.1, 255, 200, 70)

def draw_fairytail_window(scene, cx):
    # gold outer frame
    scene.add_box(cx, 21, 3.2, 2.1, 4.5, 0.2, 255, 200, 70)
    # rounded gold top
    scene.add_cylinder(cx, 23.25, 3.1, 1.05, 0.2, 255, 200, 70, rx=90)
    # transparent pink glass
    scene.add_box(cx, 21, 3.4, 1.8, 4.2, 0.1, 255, 105, 180, opacity=0.4)

    # rounded pink glass
    scene.add_cylinder(cx, 23.1, 3.4, 0.85, 0.1, 255, 105, 180, rx=90, opacity=0.4)
    # gold vertical divider
    scene.add_box(cx, 21, 3.5, 0.08, 4.2, 0.1, 255, 200, 70)
    # gold horizontal divider
    scene.add_box(cx, 21, 3.5, 1.8, 0.08, 0.1, 255, 200, 70)

def draw_rainbow_window(scene, cx):

    # gold outer circle
    scene.add_cylinder(cx, 21, 3.2, 1.75, 0.2, 255, 200, 70, rx=90)
    # pink stained glass
    scene.add_cylinder(cx, 21, 3.4, 1.5, 0.1, 255, 105, 180, rx=90, opacity=0.4)
    # raspberry inner circle
    scene.add_cylinder(cx, 21, 3.5, 1.1, 0.1, 217, 50, 81, rx=90, opacity=0.5)
    # thin gold vertical line
    scene.add_box(cx, 21, 3.6, 0.06, 3, 0.1, 255, 200, 70)
    # thin gold horizontal line
    scene.add_box(cx, 21, 3.6,3.4, 0.06, 0.1, 255, 200, 70)
    # diagonal gold lines
    scene.add_box(cx, 21, 3.6, 0.06, 3, 0.1, 255, 200, 70, rz=45)
    scene.add_box(cx, 21, 3.6, 0.06, 3, 0.1, 255, 200, 70, rz=-45)
    # gold center
    scene.add_sphere(cx, 21, 3.8, 0.2, 255, 200, 70)

def draw_grand_entrance(scene):
    #gold dorway frame
    scene.add_box(0, 3.2,3.4,2.6, 6.3, 0.2, 255, 200, 70)
    # rasberry doorway backround
    scene.add_box(0, 3.2, 3.55, 2.3)


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

