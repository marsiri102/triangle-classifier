
import math

from triangle import classify_triangle


# ACCEPT: Keep the customer scenario for a valid scalene triangle.
def test_customer_can_check_buildability_shape_and_reinforcement():
    assert classify_triangle(3, 4, 6) == "Scalene"


# ACCEPT: Keep the customer scenario for invalid dimensions.
def test_customer_receives_invalid_result_for_impossible_triangle():
    assert classify_triangle(1, 2, 3) == "Invalid"


# EDIT: Keep acceptance testing focused on customer requirements.
def test_customer_can_identify_a_right_isosceles_triangle():
    assert classify_triangle(
        5, 5, 5 * math.sqrt(2)
    ) == "Right Isosceles"


# IGNORE: Do not duplicate every unit-test case in acceptance tests.
# The detailed classification and validation cases are in test_triangle.py.
