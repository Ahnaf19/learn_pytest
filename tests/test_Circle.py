import pytest
import src.shapes as shapes

# * setup_module and teardown_module --> [run once per module] [refers to each test file]
def setup_module(module):
    print('\n')
    print("setup_module      module:%s" % module.__name__)

def teardown_module(module):
    print("teardown_module   module:%s" % module.__name__)
    
class TestCircle:
    # * setup_class and teardown_class --> [run once per class] [refers to each test class]
    def setup_class(self):
        print("setup_class      class:TestCircle")
        self.radius = 10
        self.circle = shapes.Circle(self.radius)
    
    def teardown_class(self):
        print("teardown_class   class:TestCircle")
        del self.circle # cleaing up resources
        
    # * setup_method and teardown_method --> [run once per method] [refers to each test method]
    def setup_method(self, method):
        print("setup_method    method:%s" % method.__name__)
    
    def teardown_method(self, method):
        print("teardown_method method:%s" % method.__name__) 
    
    # * name the test function test_<function_name>
    def test_area(self):
        assert self.circle.area() == 3.14 * self.radius ** 2
    
    def test_perimeter(self):
        assert self.circle.perimeter() == 2 * 3.14 * self.radius