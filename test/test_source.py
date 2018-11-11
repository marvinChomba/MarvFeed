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

        self.assertEqual(self.new_source.id,"bbc-news")

    def test_sources_list(self):
        """
        This will test whether the get_sources will return a list of sources
        """
        self.assertTrue(type(get_sources("business")) == list)
    def test_sources_category(self):
        """
        This will test whether the sources returned are of the required category
        """
        source = get_sources("health")[0]
        self.assertEqual(source.category,"health")
    