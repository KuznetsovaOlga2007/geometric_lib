import math
import pytest
import circle
import square
import triangle
from calculate import calc


class TestCircle:
    def test_circle_area(self):
        radius = 2
        expected_area = math.pi * radius ** 2
        assert circle.area(radius) == expected_area

    def test_circle_perimeter(self):
        radius = 2
        expected_perimeter = 2 * math.pi * radius
        assert circle.perimeter(radius) == expected_perimeter


class TestSquare:
    def test_square_area(self):
        side1 = 5
        side2 = 2
        assert square.area(side1) == side1 ** 2
        assert square.area(side2) == side2 ** 2

    def test_square_perimeter(self):
        side1 = 4
        side2 = 2
        assert square.perimeter(side1) == 4 * side1
        assert square.perimeter(side2) == 4 * side2


class TestTriangle:
    def test_triangle_area(self):
        base1, height1 = 6, 6
        expected_area1 = 15.588457268119896
        assert triangle.area(base1, base1, base1) == expected_area1
        
        base2, side_a, side_b = 8, 17, 15
        expected_area2 = 60
        assert triangle.area(base2, side_a, side_b) == expected_area2

    def test_triangle_perimeter(self):
        side1 = 6
        expected_perimeter1 = 18
        assert triangle.perimeter(side1, side1, side1) == expected_perimeter1
        
        side_a, side_b, side_c = 8, 17, 15
        expected_perimeter2 = 40
        assert triangle.perimeter(side_a, side_b, side_c) == expected_perimeter2


class TestCalc:
    def test_not_positive_size(self):
        with pytest.raises(ValueError):
            calc("square", "perimeter", [-5])

    def test_correct_triangle_size(self):
        with pytest.raises(ValueError):
            calc("triangle", "perimeter", [-5, 5, 0])

    def test_correct_triangle_side_value(self):
        with pytest.raises(ValueError):
            calc("triangle", "perimeter", [3, 2, 5])

    def test_correct_fig(self):
        with pytest.raises(AssertionError):
            calc("tr", "perimeter", [6, 6, 6])

    def test_correct_func(self):
        with pytest.raises(AssertionError):
            calc("triangle", "per", [6, 6, 6])

    def test_correct_size(self):
        with pytest.raises(TypeError):
            calc("triangle", "perimeter", "triangle")
