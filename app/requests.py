from app import app
import urllib.request,json
#getting api_key
Sources = sources.Sources
articles = articles.Articles

api_key = app.config['NEWS_API_KEY']