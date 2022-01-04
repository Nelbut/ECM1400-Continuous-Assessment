# =============================================================================
# Libraries
# =============================================================================
from uk_covid19 import Cov19API
import pandas as pd
import sched
import time as t
import json
import logging

# =============================================================================
# Functions
# =============================================================================

csv_filename = 'nation_2021-10-28.csv' 
def parse_csv_data(csv_filename):
    '''
    Takes in the string name of an excel document and returns a Pandas DataFrame
    '''
    logging.info("Reads excel file")
    return pd.read_csv(csv_filename)


logging.info("Reading information from json file and placing info into variables")
with open ("config.json", 'r') as info: #Retrieves information from the JSON file
    data = json.load(info)
    location = data["location"]
    location_type = data["location_type"]
    
def process_covid_csv_data(covid_csv_data):
    '''
    Takes in Pandas DataFrame and returns a list with 3 variables
    '''
    logging.info("Using Pandas to sum up all of the numbers needed")
    
    df = parse_csv_data(csv_filename)
    last7days_cases = df.loc[2][6] + df.loc[3][6] + df.loc[4][6] + df.loc[5][6] + df.loc[6][6] + df.loc[7][6] + df.loc[8][6]
    current_hospital_cases = df.loc[0][5]
    total_deaths = df.loc[13][4]
    return [int(last7days_cases), int(current_hospital_cases), int(total_deaths)]

def covid_API_request(location = location, location_type = location_type):
    '''
    Takes in 2 string variables and returns a dataframe of covid information
    '''
    logging.info("Request for Covid data")
    
    
    location_section = [
        'areaType=' + location_type,
        'areaName=' + location
    ]
    
    cases_and_deaths = {
        "date": "date",
        "areaName": "areaName",
        "areaCode": "areaCode",
        "areaType": "areaType",
        "hospitalCases":"hospitalCases",
        "cumDailyNsoDeathsByDeathDate": "cumDailyNsoDeathsByDeathDate",
        "newCasesBySpecimenDate": "newCasesBySpecimenDate"
    }
    api = Cov19API(filters=location_section, structure=cases_and_deaths)
    df = api.get_json()
    return df


scheduler = sched.scheduler(t.time, t.sleep)
def schedule_covid_updates(update_interval, update_name):
    e1 = sched.enter(update_interval, 1, covid_API_request)
    e2 = sched.enter(update_interval + 1, 1, covid_API_request, ('England, nation'))
    return e1, e2
  
# =============================================================================
# Main
# =============================================================================

covid_API_request()
[last7days_cases, current_hospital_cases, total_deaths] = process_covid_csv_data(parse_csv_data(csv_filename))

