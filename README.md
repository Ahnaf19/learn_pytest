# learn_pytest

This repository is dedicated to learning and practicing pytest, a powerful testing framework for Python. Thanks to this <a href="https://www.youtube.com/watch?v=cHYq1MRoyI0">_youtube video_</a> I got introduced with pytest and am already feeling so powerful while writing tests!

This repo definitely doesn't cover all features of pytest but contains **go to fundamentals** for writing decent test codes. These following steps outline the key concepts and features covered in this repository:

## Learning Steps

1. **Pytest Installation**:

   - Install pytest using pip: `pip install pytest`.

2. **Folder Structure**

   - the source files (files to be tested) can be on the root or inside a `source` folder
   - all test files should be inside `/tests`.
     - Add a `__init__.py` inside `/tests` so that it becomes a python module/package.
     - it can contain sub test directories.

3. **Function Based Tests**:

   - Test functions are named with the prefix `test_`.
   - Example: `test_add`, `test_subtract`, `test_multiply`, `test_divide`.
   - Fixtures can be used to create reusable test setups.

4. **Fixtures**:

   - Fixtures provide a way to provide a fixed baseline upon which tests can reliably and repeatedly execute. They help in setting up the necessary preconditions and state for tests, ensuring consistency and isolation.
   - These are globally available for all test files.
   - Example: Using `@pytest.fixture` to define a fixture.

5. **Setups and Teardowns**:

   setup and teardown module/function/class/method wrap up a module/function/class/method in a sense. The setup part comes first, then the target test and then the teardown part. Here,

   - `setup_module` and `teardown_module`: Run once per test module.
   - `setup_function` and `teardown_function`: Run once per test function.
   - `setup_class` and `teardown_class`: Run once per test class.
   - `setup_method` and `teardown_method`: Run once per test method.

6. **Class Based Tests**:

   - Test class is named with prefix `test` without any underscore.
   - Test for methods are named with prefix `test_` as usual.
   - Example methods: `test_area`, `test_perimeter`, `test_diameter`.

7. **Markers and Parametrize**:
   - There are useful markers like skip, xfail etc.
   - Custom markers can also be used to categorize tests.
   - Example: `@pytest.mark.slow` for slow tests.
   - Register custom markers in `pytest.ini`.
   - Use `@pytest.mark.parametrize` to run a test with different sets of parameters.

8. **Mock**:

   - Use the `unittest.mock` module to mock objects in your tests.
   - Example: Mocking a function or a class method.
   - _[This part is not learned yet :)]_

## Commands

9. **Run Tests**:

   - Run all tests: `pytest` [from root directory]
   - Run a specific test file: `pytest tests/test_my_functions.py`

10. **Print Setup and Teardown Messages**:

    - Use `-s` flag: `pytest tests/test_my_functions.py -s`

11. **Run Specific Test Functions with Markers**:

    - Run tests marked as slow: `pytest tests/test_my_functions.py -m slow`
    - Run tests not marked as slow: `pytest tests/test_my_functions.py -m "not slow"`

## Configuration

- `pytest.ini`: Configuration file to register custom markers.

## Let’s Connect

If you're passionate about testing or Python development, let’s discuss ideas and experiences. Feedback, forks, and collaboration requests are always welcome!
