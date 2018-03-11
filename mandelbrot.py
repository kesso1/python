"""Mandelbrot fractale visualization."""

import time
from PIL import Image


def mandelbrot_set_iterations(c_point):
    """Determine whether the point c belongs to the Mandebrot set using
       the orbit algorithm."""
    max_iter = 255
    iter_count = 0
    z = complex(0, 0)
    while (abs(z) < 2) and (iter_count < max_iter):
        z = z * z + c_point
        iter_count += 1
    return iter_count if iter_count < max_iter else 0


def iter_count_to_color(iter_count):
    """Implements a color map that translates an iteration count into
       an BGR color value."""
    red = iter_count % 4 * 64
    green = iter_count % 8 * 32
    blue = iter_count % 16 * 16
    return (red, green, blue)


def mandelbrot_fractal(*, width, height, width_pixels, height_pixels,
                       center_real, center_imag):
    """Compute the Mandelbrot fractal over two-dimensional grid."""
    image = Image.new("RGB", (width_pixels, height_pixels))
    delta_x = width / width_pixels
    delta_y = height / height_pixels
    for y in range(height_pixels):
        imag = (height_pixels / 2 - y) * delta_y + center_imag
        for x in range(width_pixels):
            z = complex((x - width_pixels / 2) * delta_x + center_real, imag)
            iter_count = mandelbrot_set_iterations(z)
            image.putpixel((x, y), iter_count_to_color(iter_count))
    return image


def main():
    """Calculates the fractal, measures the time, and writes the fractal
       image to a PNG file."""
    start_time = time.perf_counter()
    image = mandelbrot_fractal(width=3, height=2.25, width_pixels=1024,
                               height_pixels=768,
                               center_real=-0.5, center_imag=0)
    end_time = time.perf_counter()
    msg = 'computation complete in {:.3f} sec'.format(end_time - start_time)
    print(msg)
    image.save('mandel.png', 'PNG')


if __name__ == '__main__':
    main()
