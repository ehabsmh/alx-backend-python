#!/usr/bin/env python3
"""0. Parameterize a unit test"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, memoize
from typing import Dict


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    # __________________________________________________________________________

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)

# ___________________________________________________________________________________________


class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url: str, test_payload: Dict, mock_get: Mock) -> None:
        # Create response mock
        mock_response = Mock()

        # to attach a json() method that returns the expected payload
        mock_response.json.return_value = test_payload

        # and requests.get (mock) returns the response mock
        mock_get.return_value = mock_response
        response = mock_get(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(response.json(), test_payload)

# ___________________________________________________________________________________________

class TestMemoize(unittest.TestCase):
    """
    Implements a test case for utils.memoize classes
    """

    def test_memoize(self):
        """
        Method to test utils.memoize
        """
        class TestClass:
            """
            Test class for memoize
            """

            def a_method(self) -> int:
                """
                Test function
                """
                print("called a_method")
                return 42

            @memoize
            def a_property(self) -> int:
                """
                Testing memoize
                """
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_amethod:
            mock_amethod.return_value = 42
            test = TestClass()
            self.assertEqual(test.a_property, 42)
            self.assertEqual(test.a_property, 42)
            mock_amethod.assert_called_once()
