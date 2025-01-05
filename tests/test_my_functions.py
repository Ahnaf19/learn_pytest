import pytest
import time
from src.my_functions import *

# * setup_module and teardown_module --> [run once per module] [refers to each test file]
def setup_module(module):
    print('\n')
    print("setup_module      module:%s" % module.__name__)
    
def teardown_module(module):
    print("teardown_module   module:%s" % module.__name__)

# * setup_function and teardown_function --> [run once per function] [refers to each test function]
def setup_function(function):
    print("setup_function    function:%s" % function.__name__)

def teardown_function(function):
    print("teardown_function function:%s" % function.__name__)

# * name the test function test_<function_name>
def test_add():
    assert add(-1, -1) == -2
    assert add(1.5, 2.5) == 4.0

def test_subtract():
    assert subtract(1, 1) == 0
    assert subtract(-1, -1) == 0

def test_multiply():
    assert multiply(2, 2) == 4
    assert multiply(-2, 2.5) == -5.0

def test_divide():
    assert divide(4, 2) == 2
    assert divide(5, 2) == 2.5
    
# * markers
# slow test --> custom marker
# skip test --> builtin marker
# xfail test --> builtin marker

@pytest.mark.slow
def test_add_slow():
    time.sleep(2)
    assert add(1, 1) == 2

@pytest.mark.skip(reason="currently broken")
def test_subtract_skip():
    assert subtract(1, 1) == 0

@pytest.mark.xfail(reason="known issue")
def test_multiply_xfail():
    assert multiply(2, 2) == 4
    
# * run the test file
# pytest --> [auto find and run all test files]
# pytest tests/test_my_functions.py --> [run specific test file]

# * print setup and teardown messages
# pytest tests/test_my_functions.py -s

# * run specific test function with markers
# pytest tests/test_my_functions.py -m slow --> runs slow marked funtions only
# pytest tests/test_my_functions.py -m "not slow" --> runs functions not marked as slow