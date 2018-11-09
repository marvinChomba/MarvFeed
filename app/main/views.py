from ..requests import get_headlines,get_sources,get_sources_headlines,search_articles
from flask import render_template,request,url_for,redirect
from . import main

@main.route("/")
def index():

    headlines = get_headlines() 
    title = "Top Headlines"
    search_query = request.args.get("search_query")
    # search_query = "+".join(search_query.split(" "))
    if search_query:
        return redirect(url_for("main.search",search_name = search_query))
    else:
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

# @main.route("search/<search_name>")
# def search(search_name):

#     articles = search_articles(search_name)
#     title = search_name
#     return render_template("search.html",articles = articles,title = title)
