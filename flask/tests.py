import unittest
from unittest import TestCase
from server import app, db

app.config.from_object('config.TestingConfig')

if __name__ == '__main__':
    unittest.main()
