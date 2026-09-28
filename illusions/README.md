# Optical Illusions, Warm-Ups (Python + canvas2d)

Four short warm-ups to get comfortable with `canvas2d`, a simple
drawing library, and with using `for` loops to draw things. Each one
gives you a file that's almost right. It's either missing something or
has a small bug. Your job is to fix it.

## Learning Goals

- Get comfortable with `canvas2d`, a pixel-coordinate drawing library.
- Use a loop counter to control something about what gets drawn each
  time through the loop: a position, a size, or a color.
- Practice reading code someone else wrote and figuring out what's
  wrong with it, not just writing code from scratch.

## Getting the Starter Files

1. Open VSCodium.
2. If you already have a terminal tab open from a previous session,
   close it (click the trash-can icon or the "X" on it).
3. Open a new one: Terminal menu → New Terminal.
4. Check your terminal prompt (the text right before your cursor). It
   should look like this, ending in `cs50-workspace %`:
   ```
   mrsharp@Mr-Sharp cs50-workspace %
   ```
   The part before the `@` will be your own username instead, that's
   fine, but the last folder name should be `cs50-workspace`, not
   `illusions`, `illusions-part1`, or anything else.

Everything below assumes you're starting in the right place.

**If you already have an `illusions` folder from an earlier version of
this assignment**, rename it out of the way first, so the new
download doesn't collide with it:

```
mv illusions archive-illusions
```
Archive the old illusions folder

```
curl -L -O https://raw.githubusercontent.com/mrsharp-milken/illusions-part1/main/illusions-part1.zip
```
This downloads a zip file into your current folder.

```
unzip illusions-part1.zip
```
This unpacks it into a new folder called `illusions-part1`.

```
mv illusions-part1 illusions
```
This renames that folder to `illusions`. `mv` means both "move" and
"rename" in the terminal, same command either way.

```
rm illusions-part1.zip
```
Deletes the zip now that you don't need it anymore.

```
cd illusions
```
Moves you into the folder you just created.

```
python3 test_canvas2d.py
```
A window should pop up with a red circle in the middle. Close it when
you're done looking. If this works, you're ready to start the
warm-ups below.

<details>
<summary><strong>Troubleshooting</strong> (click to expand)</summary>

- **No window appears at all, or an error mentioning `tkinter`**:
  `tkinter` ships with Python, but a small number of installs are
  missing it. Try running `python3 -m tkinter` on its own. If that
  also fails to open a window, you'll need to reinstall Python from
  [python.org](https://www.python.org/downloads/), making sure not to
  skip any install options.
- **Window flickers open and immediately closes**: make sure the
  last line of your program is `canvas.wait_for_close()`. Without it,
  Python reaches the end of your script and closes the window right
  away.
- **My terminal seems frozen after I run a warm-up**: it is, on
  purpose. `canvas.wait_for_close()` keeps your program running (and
  your terminal busy) until you close the window. Close the window to
  get your terminal back, or press Ctrl+C in the terminal if you need
  it back sooner.

</details>

<details>
<summary><strong>canvas2d quick reference</strong> (click to expand)</summary>

You draw by creating a `Canvas` and calling its methods:

```python
canvas = canvas2d.Canvas(512, 512)
canvas.set_pen_color(canvas.RED)
canvas.filled_circle(256, 256, 80)
canvas.wait_for_close()
```

Every drawing function you write should take one parameter, `canvas`,
and use it the same way.

Coordinates are plain pixels. `(0, 0)` is the top-left corner of the
canvas, `x` increases to the right, and `y` increases downward. Both
range from `0` up to whatever size you passed to `Canvas(w, h)`, and
`canvas.width` / `canvas.height` hold those two numbers, so you never
need to hardcode them.

| Method | What it does |
|---|---|
| `canvas2d.Canvas(w, h)` | Open a window of the given size in pixels. Call this once, at the top of `main`. |
| `canvas.clear(color)` | Fill the whole canvas with a color. |
| `canvas.set_pen_color(color)` | Set the color used by shapes drawn after this call, e.g. `canvas.RED`. |
| `canvas.set_pen_color_rgb(r, g, b)` | Same, but as three `0`-`255` numbers instead of a named color. |
| `canvas.set_pen_width(w)` | Set line thickness, in pixels. |
| `canvas.line(x0, y0, x1, y1)` | Draw a line segment between two points. |
| `canvas.filled_circle(x, y, r)` / `canvas.circle(x, y, r)` | Filled or outlined circle, centered at `(x, y)`, radius `r`. |
| `canvas.filled_rectangle(x, y, width, height)` / `canvas.rectangle(x, y, width, height)` | Filled or outlined rectangle, centered at `(x, y)`, with the given full width and height. |
| `canvas.filled_sector(x, y, r, angle1, angle2)` / `canvas.sector(x, y, r, angle1, angle2)` | Filled or outlined "pizza slice" of a circle centered at `(x, y)` with radius `r`, from `angle1` to `angle2` in degrees (`0` pointing right, counterclockwise). |
| `canvas.pause(msec)` | Render everything drawn so far, then wait `msec` milliseconds before returning. Useful for watching a loop draw one shape at a time. |
| `canvas.wait_for_close()` | Render everything drawn so far, then leave the window open until you close it by hand. Call this once, as the last line of `main`. |

Named colors include `canvas.BLACK`, `canvas.WHITE`, `canvas.RED`,
`canvas.GREEN`, `canvas.BLUE`, `canvas.YELLOW`, `canvas.ORANGE`,
`canvas.MAGENTA`, `canvas.CYAN`, `canvas.GRAY`, among others. (They're
also available at the module level, e.g. `canvas2d.RED`, for the rare
case where you need a color and don't have a canvas on hand.)

</details>

## Warm-Ups

Do these in order. The later ones build on ideas from the earlier
ones. For each one, run the file first to see what's already there
and what's wrong with it, before you start editing.

### Warm-Up 1: Circle and Square (`warmup1_circle_square.py`)

![Circle and Square](images/warmup1.png)

`draw_circle_and_square()` draws a square with a circle inside it, but
the circle is too big: it pokes out past the square's edges instead
of touching the sides exactly. Find the line that sets the circle's
radius, and fix it so the circle is inscribed exactly inside the
square, no matter what `side` is set to.

You can run the code for this file with this command:
```
python3 warmup1_circle_square.py
```

<br/>

### Warm-Up 2: Crosshairs (`warmup2_crosshairs.py`)

![Crosshairs](images/warmup2.png)

`draw_crosshairs()` should draw a red "+" spanning the whole canvas,
but right now it only draws half of a horizontal line. Two things
need fixing: extend that line so it spans the full canvas (not just
center to the right edge), and add the missing vertical line.

Remember, to run the code in this file, run the `python3` command in terminal followed by the filename `warmup2_crosshairs.py`. Yes, I'm making you type it yourself this time so you remember!
```
python3 ________
```
_Learn the shortcuts like up-arrow key and tab-complete!_

<br/>

### Warm-Up 3: Circle Border (`warmup3_circle_border.py`)

![Circle Border](images/warmup3.png)

`draw_circle_border()` is supposed to ring the canvas with evenly
spaced green circles on all four edges. Right now it only draws the
top and bottom edges; the left and right edges are empty, and there's
no loop for them yet, you have to write one.

- The finished loop is your template: `top_bottom_x = i * 50` picks a
  different x position each time through, and it draws a circle at
  that x on both the top (`y = 0`) and bottom (`y = 500`) edges.
- Write a second loop with the same shape, but varying `y` instead of
  `x`, and drawing a circle at that `y` on both the left (`x = 0`) and
  right (`x = 500`) edges.

<br/>

### Warm-Up 4: Piano Pattern (`warmup4_piano_pattern.py`)

![Piano Pattern](images/warmup4.png)

`draw_piano_pattern()` draws the outlines of 7 white piano keys across
the canvas, but the black keys are missing. Add a filled black
rectangle between each pair of white keys, inside the existing loop.

- `key_x` already gives you the left edge of white key `i` for that
  iteration; the black key you add should be positioned relative to
  it, not hardcoded.
- Don't change `key_x` or the line that draws the white key. Don't
  change the final line in the function either; that draws the extra
  white key at the end of the row.

**Tip:** if you're not sure where a black key should land relative to
its neighbors, print `key_x` for each `i` first and sketch the numbers
on paper before touching the drawing code.

<br/>

<br/>

<br/>

## The Assignment

_Only start this section after completing the warmups!_

Pick **one** of the five optical illusions below and recreate it in
`my_illusion.py`, using `canvas2d`. That file already has the usual
`draw_my_illusion(canvas)` / `main()` structure set up; write your
illusion inside `draw_my_illusion`. Then **modify the image in some
way** to make your version distinct from what's shown: change colors,
the number of lines/shapes, line thickness, or any other modification
you like, as long as the illusion still works.


### Illusion 1: Gradient Illusion

![Gradient Illusion](images/gradient_illusion.jpg)

The background here is drawn with a gradient of gray colors ranging
from a brightness of 0 to 255. But the rectangle in the middle is one
rectangle of a single mid-intensity gray; it does not have a color
change in it!

### Illusion 2: Curving Squares

![Curving Squares](images/curving_squares.jpg)

The three purplish shapes really are squares; they are not curved.

### Illusion 3: Hering's Illusion

![Hering's Illusion](images/hering.jpg)

The red lines are not curved; they are actually straight, parallel
lines.

### Illusion 4: Eisenstein's Illusion

![Eisenstein's Illusion](images/eisenstein.jpg)

The red shapes are a true circle and a true square. Their distorted
appearance is an illusion.

### Illusion 5: Leviant Enigma

![Leviant Enigma](images/leviant_enigma.jpg)

This is a recreation of a drawing called the "Leviant Enigma." Most
people see illusory motion or flow within the purple rings. (See
[Leviant Enigma, National Gallery of Art](https://www.nga.gov/collection/art-object-page.170882.html).)

### Running and Testing Your Illusion

```
python3 my_illusion.py
```

There's no automated "correct answer" here; testing is visual:

- Confirm your image resembles the illusion you chose (compare it
  side by side with the reference image above).
- Confirm you actually see the illusion (e.g., the "gradient" bar
  looks like it changes color even though it's one solid color, the
  "curving" squares actually measure out as straight-sided, etc.).
- Confirm your required modification is present and doesn't break the
  illusion.
- Try changing a constant (like the number of lines or rings your
  loop draws) and re-running, to make sure your loop-based approach
  generalizes instead of being hardcoded shape-by-shape.
