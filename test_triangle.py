
import math
import pytest

from triangle import classify_triangle, is_valid_triangle


# ACCEPT: Use one parameterized table for classification cases.
@pytest.mark.parametrize(
    ("sides", "expected"),
    [
        ((3, 3, 3), "Equilateral"),
        ((3, 3, 4), "Isosceles"),
        ((3, 4, 5), "Right Scalene"),
        ((5, 5, 5 * math.sqrt(2)), "Right Isosceles"),
        ((2, 3, 4), "Scalene"),
        ((1, 2, 3), "Invalid"),
        ((0, 2, 2), "Invalid"),
        ((-1, 2, 2), "Invalid"),
        ((1, 1, 2.0001), "Invalid"),
    ],
)
def test_classify_triangle_cases(sides, expected):
    assert classify_triangle(*sides) == expected


# ACCEPT: Test triangle validation separately.
@pytest.mark.parametrize(
    ("sides", "expected"),
    [
        ((3, 4, 5), True),
        ((5, 3, 4), True),
        ((1, 2, 3), False),
        ((2, 2, 4), False),
        ((0, 2, 2), False),
        ((-1, 2, 2), False),
        ((1, 1, 2.0001), False),
    ],
)
def test_is_valid_triangle_cases(sides, expected):
    assert is_valid_triangle(*sides) is expected


# ACCEPT: Test right-triangle detection with different side orders.
@pytest.mark.parametrize(
    "sides",
    [
        (3, 4, 5),
        (5, 3, 4),
        (4, 5, 3),
    ],
)
def test_right_triangle_detection(sides):
    assert classify_triangle(*sides) == "Right Scalene"


# ACCEPT: Keep a floating-point right-isosceles test.
def test_right_isosceles_triangle():
    assert classify_triangle(
        5, 5, 5 * math.sqrt(2)
    ) == "Right Isosceles"


# EDIT: Test a near-degenerate triangle as valid, not invalid.
def test_near_degenerate_triangle_is_valid():
    assert classify_triangle(1, 1, 2 - 1e-12) == "Isosceles"
