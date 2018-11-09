import os

class Config():
    """
    This is the parent configuration class
    """

    HEADLINES_API  = "https://newsapi.org/v2/top-headlines?country=us&country=gb&apiKey={}"
    SOURCES_API = "https://newsapi.org/v2/sources?language=en&category={}&apiKey={}"
    SOURCES_ARTICLE_API = "https://newsapi.org/v2/top-headlines?sources={}&apiKey={}"
    SEARCH_API = "https://newsapi.org/v2/everything?q={}&apiKey={}"
    API_KEY = os.environ.get("API_KEY")

class DevConfig(Config):
    """
    This is the configurations which we will use during the development stage of the website
    """
    DEBUG = True

class ProdConfig(Config):
    """
    This is the configurations which we will use during the produciton stage of the website
    """
    pass

config_options = {
    "development": DevConfig,
    "production": ProdConfig
}