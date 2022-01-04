Introduction:
In the covid_data_handler.py module, a datraframe is read from a file and parsed.
The covid_API_request requests for covid data from an API using keywords: Covid, COVID-19 and coronavirus.

Configuration:
There is a file called config.json which stores all of the sensitive information such as the api_key.

api_key: A personalised key used to access the API which the user should creat themselves by going onto https://newsapi.org/
location: If the user doesn't input a location on the interface, the default location in the JSON file would be used.
loaction_type:If the user doesn't input a location type on the interface, the deafult location type in the JSON file would be used.
nation: If the user doesn't input a nation area on the interface then the default nation int the JSON file would be used.

covid_news_handling:
Uses a function to go 1 week into the past and retrieves information from the API using the keywords. Then the information is cut down into just the information in the articles.


User Interface:
The code for the user interface gets the API information from covid_news_handling module and displays the title and the content of the news onto the template.