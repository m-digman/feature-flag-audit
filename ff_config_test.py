import unittest
from ff_config import ff_config


class ff_config_test(unittest.TestCase):


    def setUp(self):
        self.config = ff_config("test_config.yaml")


    def test_token_returned(self):
        actual = self.config.api_token
        self.assertEqual(actual, "api-my-token")


    def test_project_returned(self):
        actual = self.config.project_key
        self.assertEqual(actual, "my-project-key")


    def test_environment_keys_returned(self):
        actual = self.config.environment_keys
        self.assertEqual(actual[0], "env1")
        self.assertEqual(actual[1], "env2")


if __name__ == '__main__':
    unittest.main()