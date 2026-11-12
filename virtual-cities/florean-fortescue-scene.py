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
    # peach colored floor ( bottom)
    scene.add_box(cx, 5, cz, 10, 10, 6, 240, 170, 148)
    # purple middle floor (middle)
    scene.add_box(cx, 13, cz, 10, 6, 6, 184, 150, 224)
    # teal top floor (top)
    scene.add_box(cx, 21, cz, 10, 10, 6, 120, 189, 184)
    # fairy arch windows (top)
    draw_fairytale_window(scene, -3.4)
    draw_fairytale_window(scene, 3.4)

    # rainbow sunburst window
    draw_rainbow_window(scene, 0)

    #long display windows
    draw_display_window(scene, 0.3)
    draw_display_window(scene, 3.4)


    def draw_fairytale_window(scene, cx):
        #deep purple outer fraim
    scene.add_box(cx, 21, 3.15, 2.1, 4.5, 0.2, 97, 55, 122)

    # round purple top
    scene.add_cylinder(cx, 23.25, 3.15, 1.05, 0.2, 97, 55, 122, rx=90)

    # Lav glass
    scene.add_box(cx, 21, 3.3, 1.7, 4.1, 0.2, 97, 55, 122, rx=90)




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

