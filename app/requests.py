import urllib.request,json
from .models import Article,Source

api_key = None
sources_api = None
headlines_api = None
sources_article_api = None
search_api = None
def configure_request(app):
    """
    This is a function that will set the configurations required for the requests
    """
    global api_key,sources_api,sources_article_api,headlines_api
    api_key = app.config["API_KEY"]
    sources_api = app.config["SOURCES_API"]
    headlines_api = app.config["HEADLINES_API"]
    sources_article_api  = app.config["SOURCES_ARTICLE_API"]
    search_api = app.config["SEARCH_API"]

def process_articles(articles):
    """
    This is a function that will process the articles list from the api into a list of Article instances
    Args:
        the list of articles
    Return:
        A list of Article instances"
    """
    results =  []
    for article in articles:
        author = article.get("author")
        description = article.get("description")
        url = article.get("url")
        image_url = article.get("urlToImage")
        publish_date = article.get("publishedAt")[0:10]
        content = article.get("content")
        title = article.get("title")
        source = article.get("source")["id"]
        if image_url and content and author:
            new_article = Article(author,title,description,url,image_url,publish_date,content,source)
            results.append(new_article)

    return results

def process_sources(sources):
    """
    This is a function that will process the sources list from the api into a list of Source instances
    Args:
        the list of sources
    Return:
        A list of Source instances"
    """

    results = []

    for source in sources:
        id = source.get("id")
        name = source.get("name")
        description = source.get("description")
        country = source.get("country")
        if description:
            new_source = Source(id,name,description,country)
            results.append(new_source)

    return results

def get_headlines():
    """
    This is a function that will get the top headlines from UK and US
    Return:
        A list of articles
    """
    headlines_url = headlines_api.format(api_key)

    with urllib.request.urlopen(headlines_url) as url:
        headlines_data = url.read()
        headlines_response = json.loads(headlines_data)

        headlines = None
        if headlines_response["articles"]:
            headlines_list = headlines_response["articles"]
            headlines = process_articles(headlines_list)

    return headlines

def get_sources(category):
    """
    This is a function that will get the sources
    Return:
        A list of sources
    """
    sources_url = sources_api.format(category,api_key)

    with urllib.request.urlopen(sources_url) as url:
        sources_data = url.read()
        sources_response = json.loads(sources_data)
    
        sources = None
        if sources_response["sources"]:
            sources_list = sources_response["sources"]
            sources = process_sources(sources_list)

    return sources

def get_sources_headlines(id):
    """
    This is a function that will get the top headlines from UK and US   
    Args:
        The id for the specific source
    Return:
        A list of articles for the specific source
    """
    sources_article_url = sources_article_api.format(id,api_key)

    with urllib.request.urlopen(sources_article_url) as url:
        headlines_data = url.read()
        headlines_response = json.loads(headlines_data)

        headlines = None
        if headlines_response["articles"]:
            headlines_list = headlines_response["articles"]
            headlines = process_articles(headlines_list)

    return headlines
        
def search_articles(search_name):

    search_url = search_api.format(search_name,api_key)

    with urllib.request.urlopen(search_url) as url:
        search_data = url.read()
        search_response = json.loads(search_data)

        results = None
        if search_response["articles"]:
            search_list = search_response["articles"]
            results = process_articles(search_list)

    return results
