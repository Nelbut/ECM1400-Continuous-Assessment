# =============================================================================
# Libraries
# =============================================================================
import requests as r
import datetime
from dateutil.relativedelta import relativedelta
import json

# =============================================================================
# Functions
# =============================================================================
def date_changer():
    '''
    returns a date 1 week in the past to be used in the url
    '''
    date = datetime.datetime.now()
    n = 1
    past_date = date - relativedelta(weeks=n)
    past_date1 = str(past_date)[:11]
    
    return past_date1

def news_API_request(date, covid_terms = 'Covid COVID-19 coronavirus'):
    '''
    Retrievs information from the API
    '''
    news = []
    base_url = r'https://newsapi.org/v2/everything?q='
    
    with open('config.json', 'r') as f:
        load = json.load(f)
        api_key = load["api_key"]
        
    for t in covid_terms.split(' '):
        url = (base_url + t + '&from=' + date + '&sortBy=publishedAt&apiKey=' + api_key)
        news_dictionary = r.get(url).json()
        articles = news_dictionary['articles']
        for i in articles:
            if i not in news:
                news.append(i)
    
    return news




def update_news():
    '''
    Updates news on template
    '''
    articles = []
    data = news_API_request(date_changer())
    for i in data:
        news_dict = {'title':i['title'], 'content':i['description']}
        articles.append(news_dict)
    return news_dict
    
    
    
def user_removed_art_head(news, headline):
    '''
    Removes news articles and headlines that the user wishes to remove
    '''
    removed = []
    removed.append(headline)
    for art in news:
        if art['title'] in removed:
            news.remove(art)
    return news

    


# =============================================================================
# Main
# =============================================================================

news = news_API_request(date_changer())

