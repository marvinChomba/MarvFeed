import unittest
from app.models import Article
from app.requests import get_headlines,get_sources_headlines
class TestArticle(unittest.TestCase):
    """
    This is a class which I'll use to run all the tests concerning news articles
    """

    def setUp(self):
        """
        This will initialize the Article class before each test
        """
        self.new_article = Article("me","Hey","None","","","","","")

    def test_init(self):
        """
        This will test whether the Article instance is instantiated correctly
        """

        self.assertTrue(self.new_article.author, "me")

    def test_return_articles(self):
        """
        This will test whether the get_headlines function returns a list of article
        """
        
        self.assertEqual(type(get_headlines()),list)

    def test_article_source(self):
        """
        This will test whether the articles received are of the required source
        """
        new_articles = get_sources_headlines("bbc-news")
        article = new_articles[0]
        self.assertEqual(article.source,"bbc-news")

    def test_article_class(self):
        """
        This will test whether the articles received are instances of the Article class
        """
        list = get_headlines()
        first_article = list[0]
        self.assertTrue(isinstance(first_article,Article))
    

    
