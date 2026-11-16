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
    draw_grand_entrance(scene)
    #gold roof piping
    scene.add_box(0, 26.3, 3.1, 10.5, 0.2, 0.5, 255, 215, 100)
    scene.add_box(0, 26.6, 3.1, 10.8, 0.2, 0.7, 255, 200, 70)
    scene.add_box(0, 26.9, 3.1, 11.2, 0.2, 0.9, 255, 225, 140)
    #pink roof stripe
    scene.add_box(0, 27.1, 3.6, 11.2, 0.1, 0.15, 255, 175, 205)
    #top floor piping
    scene.add_box(-4.85, 21, 3.1, 0.15, 9.8, 0.3, 255, 200, 70)
    scene.add_box(4.85, 21, 3.1, 0.15, 9.8, 0.3, 255, 200, 70)
    #bf piping in the corner
    scene.add_box(-4.85, 5,  3.1, 0.15, 9.8, 0.3, 255, 200, 70)
    scene.add_box(4.85, 5,  3.1, 0.15, 9.8, 0.3, 255, 200, 70)
    #uper gold border
    scene.add_box(0, 16.3, 3.1, 10.5, 0.15,  0.5, 255, 215, 100)
    scene.add_box(0, 16.6, 3.1, 10.8, 0.15, 0.7, 255, 200,70)
    #cream roof piping
    scene.add_box(0, 27.3, 3.1, 10.5, 0.12, 0.5, 255, 240, 210)
    #TF gold strips
    scene.add_box(-4.5, 21, 3.2, 0.12, 9, 0.2, 255, 225, 140)
    scene.add_box(4.5, 21, 3.2, 0.12, 9, 0.2, 255, 225, 140)
    #MF gold stripes
    scene.add_box(-4.5, 13, 3.2, 0.12, 5, 0.2, 255, 225, 140)
    scene.add_box(4.5, 13, 3.2, 0.12, 5, 0.2, 255, 225, 140)
    #roofLO
    scene.add_box(-4.3, 27.7, 3.1, 0.7, 0.7, 0.7, 255, 175, 205)
    scene.add_sphere(-4.3, 28.4, 3.1, 0.45, 255, 200, 70)
    #roofRO
    scene.add_box(4.3, 27.7, 3.1, 0.7, 0.7, 0.7, 255, 175, 205)
    scene.add_sphere(4.3, 28.4, 3.1, 0.45, 255, 200, 70)
    #small gold balls(roof)
    scene.add_sphere(-3.3, 27.6, 3.1, 0.25, 255, 200, 70)
    scene.add_sphere(-2.4, 27.6, 3.1, 0.25, 255, 200, 70)
    scene.add_sphere(2.4, 27.6, 3.1, 0.25, 255, 200, 70)
    scene.add_sphere(3.3, 27.6, 3.1, 0.25, 255, 200, 70)
    #gold pillar base
    scene.add_box(-4.1, 10.9, 3.6, 0.65, 0.3, 0.65, 255, 225, 140)
    scene.add_box(4.1, 10.9, 3.6, 0.65, 0.3, 0.65, 255, 225, 140)
    #gold pillar TOP
    scene.add_box(-4.1, 15.8, 3.6, 0.65, 0.3, 0.65, 255, 225, 140)
    scene.add_box(4.1, 15.8, 3.6, 0.65, 0.3, 0.65, 255, 225, 140)
    #pink wall stuff
    scene.add_box(-3.7, 13.3, 3.2, 0.12, 4.5, 0.2, 255, 155, 185)
    scene.add_box(3.7, 13.3, 3.2, 0.12, 4.5, 0.2, 255, 155, 185)
    #extra gold stripes
    scene.add_box(0, 17.2, 3.1, 10, 0.12, 0.3, 255, 200, 70)
    scene.add_box(0, 25.2, 3.1, 10, 0.12, 0.3, 255, 200, 70)
    #cream stripes
    scene.add_box(0, 17.4, 3.1, 10, 0.1, 0.3, 255, 235, 210)
    scene.add_box(0, 25.45, 3.1, 10, 0.1, 0.3, 255, 235, 210)
    #gold roof caps
    scene.add_box(-4.9, 26.3, 3.1, 0.5, 0.6, 0.7, 255, 200, 70)
    scene.add_box(4.9, 26.3, 3.1, 0.5, 0.6, 0.7, 255, 200, 70)

    #living wall
    scene.add_box(0, 13, 3.2, 7.3, 4.5, 0.2, 45, 110, 65)
    scene.add_box(0, 13, 3.35, 6.8, 4, 0.1, 65, 140, 75)

    #green wall+gold border
    scene.add_box(0, 15.3, 3.5, 7.6, 0.15, 0.2, 255, 200, 70)
    scene.add_box(0, 10.7, 3.5, 7.6, 0.15, 0.2, 255, 200, 70)
    scene.add_box(-3.7, 13, 3.5, 0.15, 4.6, 0.2, 255, 200, 70)
    scene.add_box(3.7, 13, 3.5, 0.15, 4.6, 0.2, 255, 200, 70)
    #leavesfor LW
    scene.add_sphere(-2.8, 14.5, 3.6, 0.55, 35, 125, 65)
    scene.add_sphere(-1.6, 14.7, 3.6, 0.65, 50, 155, 75)
    scene.add_sphere(-0.3, 14.4, 3.6, 0.55, 35, 125, 65)
    scene.add_sphere(1, 14.7, 3.6, 0.65, 50, 155, 75)
    scene.add_sphere(2.5, 14.5, 3.6, 0.55, 35, 125, 65)
    #low leaves
    scene.add_sphere(-2.6, 11.6, 3.6, 0.6, 50, 155, 75)
    scene.add_sphere(-1.2, 11.4, 3.6, 0.55, 35, 125, 65)
    scene.add_sphere(0.3, 11.6, 3.6, 0.65, 50, 155, 75)
    scene.add_sphere(1.7, 11.4, 3.6, 0.55, 35, 125, 65)
    scene.add_sphere(2.8, 11.6, 3.6, 0.6, 50, 155, 75)

    #flowers(hydrangas aka my favorite flower in the world)
    #pink
    scene.add_sphere(-2.3, 13.6, 3.9, 0.5, 255, 105, 180)
    scene.add_sphere(-1.9, 13.9, 3.9, 0.35, 255, 190, 220)
    scene.add_sphere(-2.6, 13.9, 3.9, 0.25, 235, 65, 145)
    #purple
    scene.add_sphere(0, 13.4, 3.9, 0.5, 190, 155, 235)
    scene.add_sphere(0.4, 13.7, 3.9, 0.35, 225, 195, 255)
    scene.add_sphere(-0.4, 13.7, 3.9, 0.35, 145, 95, 205)
    #blue
    scene.add_sphere(2.3, 13.6, 3.9, 0.5, 135, 195, 255)
    scene.add_sphere(2.7, 13.9, 3.9, 0.35, 175, 220, 255)
    scene.add_sphere(1.9, 13.9, 3.9, 0.35, 105, 165, 235)
    #gold floor on balcony
    scene.add_box(0, 10.4, 4.2, 8.5, 0.3, 2, 255, 200, 70)
    #pink floor on B
    scene.add_box(0, 10.6, 4.2, 8.1, 0.15, 1.8, 255, 175, 205)
    #gold railing on B
    scene.add_box(0, 12, 5.1, 8.5, 0.15, 0.2, 255, 200, 70)
    scene.add_box(0, 10.9, 5.1, 8.5, 0.15, 0.2, 255, 200, 70)
    #gold posts on B
    scene.add_cylinder(-3.8, 11.5, 5.1, 0.1, 1.2, 255, 200, 70)
    scene.add_cylinder(-2.5, 11.5, 5.1, 0.1, 1.2, 255, 200, 70)
    scene.add_cylinder(-1.2, 11.5, 5.1, 0.1, 1.2, 255, 200, 70)
    scene.add_cylinder(0, 11.5, 5.1, 0.1, 1.2, 255, 200, 70)
    scene.add_cylinder(1.2, 11.5, 5.1, 0.1, 1.2, 255, 200, 70)
    scene.add_cylinder(2.5, 11.5, 5.1, 0.1, 1.2, 255, 200, 70)
    scene.add_cylinder(3.8, 11.5, 5.1, 0.1, 1.2, 255, 200, 70)

    #giant ice cream cone
    #gold stand
    scene.add_cylinder(0, 27.3, 0, 2, 0.5, 255, 200, 70)
    #pink stand
    scene.add_cylinder(0, 27.7, 0, 1.7, 0.3, 255, 175, 205)
    #waffle cone
    scene.add_cone(0, 30, 0, 1.5, 4, 225, 175, 105, rx=180)
    #strawberry
    scene.add_sphere(0, 32.2, 0, 1.7, 255, 145, 190)
    #lav
    scene.add_sphere(0, 33.6, 0, 1.4, 195, 160, 245)
    #vanela
    scene.add_sphere(0, 34.8, 0, 1.1, 255, 240, 210)
    #cherry on top
    scene.add_sphere(0, 35.9, 0, 0.45, 225, 45, 85)




    #purple shop on left
    scene.add_box
    scene.add_box
    scene.add_box
    scene.add_box
    scene.add_box
    scene.add_sphere

    scene.add_box
    scene.add_box
    scene.add_box
    scene.add_box
    scene.add_box
    scene.add_sphere

    scene.add_box
    scene.add_box
    scene.add_box
    scene.add_box
    scene.add_box
    scene.add_sphere

    scene.add_box
    scene.add_box
    scene.add_box
    scene.add_box
    scene.add_box
    scene.add_sphere


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

    # pastel rainbow glass
    scene.add_box(-0.7, 21.7, 3.7, 0.45, 0.45, 0.1, 255, 145, 185)
    scene.add_box(0, 21.7, 3.7, 0.45, 0.45, 0.1, 255, 195, 120)
    scene.add_box(0.7, 21.7, 3.7, 0.45, 0.45, 0.1, 255, 235, 140)

    scene.add_box(-0.7, 21, 3.7, 0.45, 0.45, 0.1, 175, 225, 165)
    scene.add_box(0, 21, 3.7, 0.45, 0.45, 0.1, 145, 205, 255)
    scene.add_box(0.7, 21, 3.7, 0.45, 0.45, 0.1, 190, 155, 235)

    scene.add_box(-0.7, 20.3, 3.7, 0.45, 0.45, 0.1, 255, 185, 220)
    scene.add_box(0, 20.3, 3.7, 0.45, 0.45, 0.1, 175, 235, 225)
    scene.add_box(0.7, 20.3, 3.7, 0.45, 0.45, 0.1, 225, 185, 255)



    # blocky pastel rainbow glass



    # gold center
    scene.add_sphere(cx, 21, 3.8, 0.2, 255, 200, 70)

def draw_grand_entrance(scene):
    #gold dorway frame
    scene.add_box(0, 3.2,3.4,2.6, 6.3, 0.2, 255, 200, 70)
    # rasberry doorway backround
    scene.add_box(0, 3.2, 3.55, 2.3, 6, 0.1, 150, 35, 75)
    #pink double doors
    scene.add_box(-0.58, 3.1, 3.65, 1.05, 5.7, 0.1, 255, 165, 195)
    scene.add_box(0.58, 3.1, 3.65, 1.05, 5.7, 0.1, 255, 165, 195)
    #gold mid div
    scene.add_box(0, 3.1, 3.75, 0.08, 5.8, 0.1, 225, 200, 70)

    #transparent glass panels
    scene.add_box(-0.58, 3.8, 3.75, 0.8, 2.3, 0.05, 255, 225, 240, opacity=0.5)
    scene.add_box(0.58, 3.8, 3.75, 0.8, 2.3, 0.05, 255, 225, 240, opacity=0.5)

    #gold door handels
    scene.add_sphere(-0.15, 2.8, 3.85, 0.1, 255, 200, 70)
    scene.add_sphere(0.15, 2.8, 3.85, 0.1, 255, 200, 70)

    #gold door decor
    scene.add_box(-0.58, 2.1, 3.77, 0.8, 0.07, 0.05, 255, 200, 70)
    scene.add_box(0.58, 2.1, 3.77, 0.8, 0.07, 0.05, 255, 200, 70)

    #gold colloms
    scene.add_cylinder(-1.5, 3.3, 3.7, 0.15, 6.5, 255, 200, 70)
    scene.add_cylinder(1.5, 3.3, 3.7, 0.15, 6.5, 255, 200, 70)

    #gold decor
    scene.add_sphere(-1.5, 6.55, 3.7, 0.22, 255, 200, 70)
    scene.add_sphere(1.5, 6.55, 3.7, 0.22, 255, 200, 70)

    #gold beam
    scene.add_box(0, 6.5, 3.7, 3.5, 0.3, 0.6, 255, 200, 70)

    #pink awning
    scene.add_box(0, 7.05, 3.8, 4.4, 0.7, 1.25, 255, 155, 185)

    #gold awning trimmmm
    scene.add_box(0, 7.45, 3.8, 4.55, 0.12, 1.32, 255, 200, 70)
    scene.add_box(0, 6.7, 4.45, 4.55, 0.12, 0.12, 255, 200, 70)

    #gold decor
    scene.add_sphere(-1.8, 6.65, 4.5, 0.12, 255, 200, 70)
    scene.add_sphere(-0.9, 6.65, 4.5, 0.12, 255, 200, 70)
    scene.add_sphere(0, 6.65, 4.5, 0.12, 255, 200, 70)
    scene.add_sphere(0.9, 6.65, 4.5, 0.12, 255, 200, 70)
    scene.add_sphere(1.8, 6.65, 4.5, 0.12, 255, 200, 70)

    #Ice cream sign
    scene.add_box(0, 8.2, 3.4, 4.4, 1, 0.2, 255, 200, 70)
    scene.add_box(0, 8.2, 3.55, 4.1, 0.75, 0.1, 145, 35, 75)

    #sign decor
    scene.add_sphere(-1.85, 8.2, 3.65, 0.12, 255, 200, 70)
    scene.add_sphere(1.85, 8.2, 3.65, 0.12, 255, 200, 70)



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

