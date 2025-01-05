import pytest
# import src.shapes as shapes

# * fixtures can be defined in a separate 'conftest.py' file
# @pytest.fixture
# def rectangle():
#     return shapes.Rectangle(length=10, width=20)

# @pytest.fixture
# def weird_rectangle():
#     return shapes.Rectangle(length=5, width=6)

def test_area(rectangle):
    # rectangle = shapes.Rectangle(length=10, width=20)
    assert rectangle.area() == 200
    
def test_perimeter(rectangle):
    # rectangle = shapes.Rectangle(length=10, width=20)
    assert rectangle.perimeter() == 2 * (10 + 20)
    
def test_not_equal(rectangle, weird_rectangle):
    # rectangle = shapes.Rectangle(length=10, width=20)
    # weird_rectangle = shapes.Rectangle(length=5, width=6)
    assert rectangle != weird_rectangle