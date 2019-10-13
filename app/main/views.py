from flask import  render_template
from app import app
from .requests import get_sources

#Views
@app.route('/')
def index():
    
    '''
    
    View root page function that returns the index page and  its data
    
    '''
    #getting the sources
    news_sources = get_sources(category)
    print(news_sources)
    
    
    
    title = 'Home - Welcome to the newshighlights website'
    return render_template('index.html', title = title, category = news_sources)

@app.route('/news/<int:news_id>')
def news(news_id):
    
    '''
    Views the news page functionality that returns newshighlightd details and its data
    
    '''
    title = 'Home - Welcome to the newshighlights website'
    return render_template('news.html', id = news_id, title = title)