from ..requests import get_headlines,get_sources,get_sources_headlines,search_articles
from flask import render_template,request,url_for,redirect
from . import main

@main.route("/")
def index():
    """
    View function for the landing page
    """
    headlines = get_headlines() 
    title = "Top Headlines"
    return render_template("index.html", headlines=headlines,title=title)

@main.route("/sources/<category>")
def sources(category):
    """
    View function for the source pages
    """
    sources = get_sources(category)
    title = category.capitalize()
    header = category.capitalize()
    return render_template("sources.html",sources = sources,title = title,header = header)

@main.route("/sources/articles/<id>")
def source_articles(id):
    """
    View function for a specific source's articles
    """
    articles = get_sources_headlines(id)
    header = id.split("-")
    new_head = []
    for head in header:
        new_head.append(head.upper())
    final_header = " ".join(new_head)

    return render_template("source_articles.html",articles = articles,header = final_header,title=final_header)

