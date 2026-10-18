import math


def is_valid_triangle(a, b, c):
    sides = (a, b, c)

    if any(
        isinstance(side, bool)
        or not isinstance(side, (int, float))
        or not math.isfinite(side)
        or side <= 0
        for side in sides
    ):
        return False

    x, y, z = sorted(sides)
    return x + y > z


def classify_triangle(a, b, c):
    if not is_valid_triangle(a, b, c):
        return "Invalid"

    x, y, z = sorted((a, b, c))

    is_right = math.isclose(
        x * x + y * y,
        z * z,
        rel_tol=1e-9,
        abs_tol=1e-9,
    )

    if x == z:
        return "Equilateral"

    if x == y or y == z:
        if is_right:
            return "Right Isosceles"
        return "Isosceles"

    if is_right:
        return "Right Scalene"

    return "Scalene"