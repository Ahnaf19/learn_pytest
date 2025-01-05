import pytest
from src import shapes as shapes

# * pytest auto reads the conftest.py file and fixtures inside, making them available to all test files globally

@pytest.fixture
def rectangle():
    return shapes.Rectangle(length=10, width=20)

@pytest.fixture
def weird_rectangle():
    return shapes.Rectangle(length=5, width=6)