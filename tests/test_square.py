import pytest
import src.shapes as shapes

# * parametrize the marker for multiple test cases
# alternative to for loop

@pytest.mark.parametrize("side, area", [(10, 100), (20, 400), (30, 900)])
def test_area(side, area):
    assert shapes.Square(side=side).area() == area
    