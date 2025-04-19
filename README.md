## Hexagon Spiral of Hexagon Spirals
This Python program generates a visually captivating spiral pattern made of smaller hexagon spirals using the Turtle Graphics module. The final artwork is saved as a high-quality PNG image using the Pillow library.
## Output Preview
The final output is a complex fractal-like spiral image saved as ```spiral.png```.
## Features
Recursively draws spiraling hexagon patterns.

Uses trigonometric calculations for realistic spiral geometry.

Optimized rendering with ```screen.tracer()``` for faster drawing.

Saves the output image in PNG format using Pillow.
## Requirements
Python 3.x

turtle (comes built-in with Python)

Pillow for image conversion (pip install pillow)
## 📁 Files
```spiral.py``` – The main script that draws and saves the image.

```spiral.png``` – The final output image (generated after running the script).

##  How It Works
The program initializes the Turtle Graphics screen and sets up the canvas.

The recursive draw_spiral() function calculates and draws hexagon-based spiral paths with a twist angle (alpha).

It uses trigonometry to manage direction and distance for drawing.

Once complete, the canvas is saved as an EPS file, then converted to a PNG using Pillow.
