import unittest
from app.models import Source
from app.requests import get_sources
class TestSource(unittest.TestCase):
    """
    This is where I will run all the tests for the sources
    """
    def setUp(self):
        """
        This will run before each test
        """
        self.new_source = Source("bbc-news","halo","","","")

    def test_init(self):
        """
        This will test whether the Source instance is instantiated correctly
        """

        self.assertTrue(self.new_source.id,"bbc-news")


    