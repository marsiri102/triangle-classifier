# Triangle Classifier

This project checks if three side lengths can make a triangle. It also tells you what type of triangle it is and if it is a right triangle.

## Triangle Types

- Equilateral: All three sides are equal.
- Isosceles: Exactly two sides are equal.
- Scalene: All three sides are different.
- Invalid: The sides cannot make a triangle.
- Right triangle: The triangle has a 90 degree angle, so the result starts with "Right ".

An equilateral triangle cannot be a right triangle because all three of its angles are 60 degrees. A right triangle must have one 90 degree angle.

## Equivalence Classes and Boundaries

These are the different types of inputs I tested.

- Equilateral triangle: (3, 3, 3)
- Isosceles triangle: (3, 3, 4)
- Scalene triangle: (2, 3, 4)
- Right triangle: (3, 4, 5)
- Right isosceles triangle: (5, 5, 5 * sqrt(2))
- Zero side: (0, 2, 2), which is invalid.
- Negative side: (-1, 2, 2), which is invalid.
- Degenerate triangle: (1, 2, 3), which is invalid because two sides add up to the third side.
- Near the boundary: (1, 1, 2 - 1e-12), which is still a valid triangle.

## Acceptance Criteria

1. When a customer enters sides that make a valid triangle, the program returns the correct type.
2. When the sides cannot make a triangle, the program returns "Invalid" without crashing.
3. When a triangle is a right triangle, the result starts with "Right " so the studio knows it needs reinforced corners.

## Copilot Review Log

- ACCEPT: Used one table of test cases to check different triangle types.
- ACCEPT: Separated the validation tests from the classification tests.
- ACCEPT: Tested right triangles with the sides in different orders.
- EDIT: Used math.isclose() to check right triangles because decimal calculations can be slightly different. This should only be listed if it matches a suggestion I actually reviewed.
- EDIT: Changed the near-degenerate test because the triangle is still valid when the two shorter sides add up to more than the longest side.
- IGNORE: Avoided repeating every unit test in the acceptance tests.

## Running the Tests

Install pytest:

```bash
py -m pip install pytest
```

Run the tests:

```bash
py -m pytest test_triangle.py test_acceptance.py -v
```

## AI Use

- ChatGPT: Helped with the code, test examples, README, and fixing Python and pytest errors.
- GitHub Copilot: Used in VS Code to suggest unit tests. I reviewed the suggestions and accepted, edited, or rejected them.
- Acceptance tests: I worked on the customer requirements and acceptance test without using Copilot, as required by the assignment.
- Testing: I ran the tests with pytest, and all tests passed.