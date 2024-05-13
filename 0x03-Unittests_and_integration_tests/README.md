<p align="center">
  <img src="https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png" />
</p>

# This project incorporates a comprehensive testing strategy that leverages both unit tests and integration tests to ensure the quality and reliability of the back-end code.

## Tasks

### [0. Parameterize a unit test](https://github.com/ehabsmh/alx-backend-python/blob/main/0x03-Unittests_and_integration_tests/test_utils.py)
Familiarize yourself with the `utils.access_nested_map` function and understand its purpose. Play with it in the Python console to make sure you understand.

In this task you will write the first unit test for `utils.access_nested_map`.

Create a `TestAccessNestedMap` class that inherits from `unittest.TestCase`.

Implement the `TestAccessNestedMap.test_access_nested_map` method to test that the method returns what it is supposed to.

Decorate the method with `@parameterized.expand` to test the function for following inputs:

```py
nested_map={"a": 1}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a", "b")
```
For each of these inputs, test with `assertEqual` that the function returns the expected result.

The body of the test method should not be longer than 2 lines.

---

### 1. Parameterize a unit test](https://github.com/ehabsmh/alx-backend-python/blob/main/0x03-Unittests_and_integration_tests/test_utils.py)
Implement `TestAccessNestedMap.test_access_nested_map_exception`. Use the `assertRaises` context manager to test that a `KeyError` is raised for the following inputs (use `@parameterized.expand`):

```py
nested_map={}, path=("a",)
nested_map={"a": 1}, path=("a", "b")
```
Also make sure that the exception message is as expected.