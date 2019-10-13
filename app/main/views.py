from flask import  render_template,redirect,url_for,request
from . import main
from ..models import Sources
from .requests import get_sources

#Views
@main.route('/')
def index():
    
    '''
    
    View root page function that returns the index page and  its data
    
    '''
    #getting the sources
    news_sources = get_sources(category)
    print(news_sources)
    
    
    
    title = 'Home - Welcome to the newshighlights website'
    return render_template('index.html', title = title, category = news_sources)

@main.route('/news/<int:news_id>')
def news(news_id):
    
    '''
    Views the news page functionality that returns newshighlightd details and its data
    
    '''
    title = 'Home - Welcome to the newshighlights website'
    return render_template('news.html', id = news_id, title = title)