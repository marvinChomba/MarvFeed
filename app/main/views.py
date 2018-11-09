from ..requests import get_headlines,get_sources,get_sources_headlines
from flask import render_template
from . import main

@main.route("/")
def index():

    headlines = get_headlines() 
    title = "Top Headlines"

    return render_template("index.html", headlines=headlines,title=title)

@main.route("/sources/<category>")
def sources(category):

    sources = get_sources(category)
    title = category.capitalize()
    return render_template("sources.html",sources = sources,title = title)

@main.route("/sources/articles/<id>")
def source_articles(id):
    articles = get_sources_headlines(id)
    
    return render_template("source_articles.html",articles = articles)