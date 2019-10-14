from flask import  render_template,redirect,url_for,request
from . import main
from ..models import Sources
from ..requests import get_sources, get_articles


#Views
@main.route('/')
def index():
    
    '''
    
    View root page function that returns the index page and  its data
    
    '''
    source = get_sources()
    
    title = 'Home - Welcome to the newshighlights website'
    return render_template('index.html', title = title, source = source)

@main.route('/news')
def news():
    
    '''
    Views the news page functionality that returns newshighlightd details and its data
    
    '''
    articles = get_articles()
    title = 'Home - Welcome to the newshighlights website'
    return render_template('news.html', articles=articles, title = title)

