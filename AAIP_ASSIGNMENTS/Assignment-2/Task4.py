import math
from typing import Literal

def area_circle(radius: float) -> float:
    """Return area of a circle given its radius."""
    if radius < 0:
        raise ValueError("radius must be non-negative")
    return math.pi * radius * radius

def area_rectangle(width: float, height: float) -> float:
    """Return area of a rectangle given width and height."""
    if width < 0 or height < 0:
        raise ValueError("width and height must be non-negative")
    return width * height

def area_triangle(base: float, height: float) -> float:
    """Return area of a triangle given base and height."""
    if base < 0 or height < 0:
        raise ValueError("base and height must be non-negative")
    return 0.5 * base * height

def area_trapezoid(a: float, b: float, height: float) -> float:
    """Return area of a trapezoid with parallel sides a and b and given height."""
    if a < 0 or b < 0 or height < 0:
        raise ValueError("sides and height must be non-negative")
    return 0.5 * (a + b) * height

def area_ellipse(a: float, b: float) -> float:
    """Return area of an ellipse with semi-axes a and b."""
    if a < 0 or b < 0:
        raise ValueError("semi-axes must be non-negative")
    return math.pi * a * b

def area(shape: Literal['circle','rectangle','triangle','trapezoid','ellipse'], **kwargs) -> float:
    """
    Generic dispatcher to compute area for supported shapes.
    Call examples:
      area('circle', radius=3)
      area('rectangle', width=4, height=5)
    """
    if shape == 'circle':
        return area_circle(kwargs['radius'])
    if shape == 'rectangle':
        return area_rectangle(kwargs['width'], kwargs['height'])
    if shape == 'triangle':
        return area_triangle(kwargs['base'], kwargs['height'])
    if shape == 'trapezoid':
        return area_trapezoid(kwargs['a'], kwargs['b'], kwargs['height'])
    if shape == 'ellipse':
        return area_ellipse(kwargs['a'], kwargs['b'])
    raise ValueError(f"Unsupported shape: {shape}")

if __name__ == "__main__":
    print("Supported shapes: circle, rectangle, triangle, trapezoid, ellipse")
    shape = input("Enter shape: ").strip().lower()
    try:
        if shape == 'circle':
            r = float(input("Enter radius: ").strip())
            print(f"Area = {area('circle', radius=r)}")
        elif shape == 'rectangle':
            w = float(input("Enter width: ").strip())
            h = float(input("Enter height: ").strip())
            print(f"Area = {area('rectangle', width=w, height=h)}")
        elif shape == 'triangle':
            b = float(input("Enter base: ").strip())
            h = float(input("Enter height: ").strip())
            print(f"Area = {area('triangle', base=b, height=h)}")
        elif shape == 'trapezoid':
            a = float(input("Enter side a: ").strip())
            b = float(input("Enter side b: ").strip())
            h = float(input("Enter height: ").strip())
            print(f"Area = {area('trapezoid', a=a, b=b, height=h)}")
        elif shape == 'ellipse':
            a = float(input("Enter semi-axis a: ").strip())
            b = float(input("Enter semi-axis b: ").strip())
            print(f"Area = {area('ellipse', a=a, b=b)}")
        else:
            print("Unsupported shape")
    except (ValueError, KeyError) as e:
        print("Error:", e)
