#!/usr/bin/env python3
"""0. Parameterize a unit test"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json


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
    def test_get_json(self, url, expected, mock_get):
        # Create response mock
        mock_response = Mock()

        # to attach a json() method that returns the expected payload
        mock_response.json.return_value = expected

        # and requests.get (mock) returns the response mock
        mock_get.return_value = mock_response

        mock_get.assert_called_once_with(url)
        self.assertEqual(get_json(url), expected)
