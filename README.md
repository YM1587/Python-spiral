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

The recursive ```draw_spiral()``` function calculates and draws hexagon-based spiral paths with a twist angle ```(alpha).```

It uses trigonometry to manage direction and distance for drawing.

Once complete, the canvas is saved as an EPS file, then converted to a PNG using Pillow.
##  How to Run
Install dependencies:
```
bash 
pip install pillow
```
Run the script:
```
bash 
python spiral.py
```
Check your project directory for spiral.png.
## Sample Spiral Output
A hypnotic, colorful pattern of interlocking spirals—ideal for artistic or generative design experiments.
## What is Pillow?
<b>Pillow</b>  is a powerful and easy-to-use Python Imaging Library (PIL) fork that allows you to open, manipulate, and save many different image file formats. It’s widely used in tasks like:

Image conversion (e.g., EPS to PNG)

Cropping, resizing, rotating, and flipping images

Drawing shapes or text on images

Applying filters and effects

Automating image processing workflows

Pillow is the go-to library in Python for working with images in a programmatic way.
##  Why Is Pillow Used in This Project?
In your spiral drawing program, you use Turtle Graphics to create a visual pattern. Turtle’s default way of saving images is in EPS (Encapsulated PostScript) format, which is great for vector-based graphics but not easily viewable in many everyday applications.

That’s where Pillow comes in — it handles the EPS file and converts it to a more user-friendly format like PNG, which is widely supported and can be shared or posted online.
## How It’s Used:
```
from PIL import Image

# Load the EPS file created by turtle graphics
img = Image.open("spiral.eps")

# Save the image in PNG format
img.save("spiral.png", "PNG")

```
So basically:

Turtle draws the spiral and saves it as an .eps file.

Pillow opens that .eps file and saves it as .png.

## Supported File Formats
Pillow supports a wide range of file formats, including:

PNG, JPEG, GIF, BMP, TIFF

EPS, PDF, ICO, WEBP

and more...

This makes it a versatile choice for any kind of image processing in Python.
## Additional Features
Here are just a few of the powerful things you can do with Pillow:

Convert between formats

Resize or crop images

Add filters or watermarks

Generate thumbnails

Draw shapes, lines, or text on images

If you ever want to expand your program to add titles, effects, or even watermark your spiral images, Pillow can help with that too!

## Fun Fact
This pattern uses properties of regular hexagons and clever recursion to simulate a natural spiral structure, often found in plants, shells, and galaxies.

## 📝 License
This project is open-source and free to use for educational or creative purposes.
