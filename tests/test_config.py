import unittest
from config import CORSConfig, AppConfig


class TestCORSConfig(unittest.TestCase):
    def test_cors_origins(self):
        expected_origins = ['http://example.com', 'http://another-example.com']
        self.assertEqual(CORSConfig.ORIGINS, expected_origins)

    def test_cors_methods(self):
        expected_methods = ['GET', 'POST', 'PUT', 'DELETE']
        self.assertEqual(CORSConfig.METHODS, expected_methods)

    def test_cors_allow_headers(self):
        expected_headers = ['Authorization', 'Content-Type']
        self.assertEqual(CORSConfig.ALLOW_HEADERS, expected_headers)

    def test_cors_supports_credentials(self):
        self.assertFalse(CORSConfig.SUPPORTS_CREDENTIALS)

    def test_cors_max_age(self):
        self.assertEqual(CORSConfig.MAX_AGE, 3600)

    def test_cors_send_wildcard(self):
        self.assertFalse(CORSConfig.SEND_WILDCARD)

    def test_cors_automatic_options(self):
        self.assertFalse(CORSConfig.AUTOMATIC_OPTIONS)

    def test_cors_vary_header(self):
        self.assertTrue(CORSConfig.VARY_HEADER)


class TestAppConfig(unittest.TestCase):
    def test_api_key(self):
        expected_api_key = "your_secret_api_key"
        self.assertEqual(AppConfig.API_KEY, expected_api_key)


if __name__ == "__main__":
    unittest.main()
