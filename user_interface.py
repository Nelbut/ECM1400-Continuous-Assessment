# =============================================================================
# Libraries
# =============================================================================

from flask import Flask
from flask import render_template
from covid_news_handling import news
import json
from covid_data_handler import last7days_cases

# =============================================================================
# Functions
# =============================================================================

app = Flask(__name__)

with open('config.json', 'r') as f: #Retrieves information from the JSON file
    info = json.load(f)
    image = info["image"]
    location = info["location"]




titles = [Dict['title'] for Dict in news]
content = [Dict['description'] for Dict in news]
  

@app.route('/index')
def template():
    '''
    Renderes information to the index.html template for the user
    '''    
    info =[
        {
          "title": titles[0],
          "content": content[0]
          },
        {
          "title": titles[1],
          "content": content[1]
          },
        {
          "title": titles[2],
          "content": content[2]
          },
        {
          "title": titles[3],
          "content": content[3]
          },
        {
          "title": titles[4],
          "content": content[4]
          }
        ]
    return render_template('index.html',
                           title = "Daily update",
                           image = image,
                           location = location,
                           local_7day_infections = last7days_cases,
                           news_articles = info)

if __name__ == '__main__':
    app.run()


# =============================================================================
# Main
# =============================================================================


 
