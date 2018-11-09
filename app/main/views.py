from ..requests import get_headlines,get_sources,get_sources_headlines
from flask import render_template
from . import main

@main.route("/")
def index():

    headlines = get_headlines() 
    title = "Top Headlines"

    return render_template("index.html", headlines=headlines,title=title)

