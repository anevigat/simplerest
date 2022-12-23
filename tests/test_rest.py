"""Test for rest api."""
import json
import os
import unittest
from http import HTTPStatus

from main import app


class TestCalc(unittest.TestCase):
    """Class for testing REST API."""

    def setUp(self):
        """Set dictionary for testing and start router."""
        self.info = {}
        self.client = app.test_client()

    def test_should_return_hello(self):
        """Test for testing base route"""
        url = '/'
        response = self.client.get(url)
        self.assertEqual(b'Hello from Test', response.get_data())
        self.assertEqual(200, response.status_code)

    def test_should_return_dictionary(self):
        """Test for testing /info route"""
        url = '/info'
        response = self.client.get(url)
        expected = {
            'app_name': os.environ.get('APP_NAME'),
            'version': os.environ.get('VERSION'),
            'namespace': os.environ.get('NAMESPACE'),
            'pod': os.environ.get('POD'),
            'node': os.environ.get('NODE'),
            'connect_url': os.environ.get('CONNECT_URL')
        }
        self.assertDictEqual(expected, json.loads(response.get_data()))

    def test_should_return_200_when_external_conn(self):
        """Test for testing /connect route"""
        url = '/connect'
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)
