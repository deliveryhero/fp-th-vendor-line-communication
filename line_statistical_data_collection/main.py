import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, parentdir + '/src')
from get_secrete_token import get_secret_data
import requests
import urllib.parse
import pandas as pd
from datetime import datetime, timedelta
from datetime import date
import numpy as np
from bigquery_data import insert_line_statistical_data

slack_webhook = os.getenv('slack_webhook')
CHANNEL_ACCESS_TOKEN = get_secret_data()

def get_message_delivery_statistics(params):
    headers = {
        "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}"
    }
    value = params['customAggregationUnit']
    params = urllib.parse.urlencode(params)
    url = "https://api.line.me/v2/bot/insight/message/event/aggregation"

    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        delivery_data = response.json()
        return delivery_data
    else:
        
        requests.post(slack_webhook,
              json = {'text' : '*line_statistiacal_data_collection: Failed get line data: ' + f"Error: {value} - {response.status_code} - {response.text}"})
        return None

if __name__ == "__main__":
    date_now = datetime.now()
    date_now = datetime.strftime(date_now, '%Y-%m-%d %H:%M:%S')
    yesterday_date = datetime.now() - timedelta(1)
    collection_date = date.today() - timedelta(1)
    yesterday = datetime.strftime(yesterday_date, '%Y%m%d')
    headers = {
        "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}"
    }
    url_1 = "https://api.line.me/v2/bot/message/aggregation/list"

    params = {
        'limit':'100'
    }
    try:
      response = requests.get(url_1, headers=headers,params=params)
      delivery_data = response.json()
    except BaseException as e:
      requests.post(slack_webhook,
      json = {'text' : '*line_statistiacal_data_collection*: Failed to get list of line pipelines from line: ' + str(e)})
        
    final_df = pd.DataFrame()
    for i in delivery_data['customAggregationUnits']:
        params_1 = {
            'customAggregationUnit': i,
            'from': yesterday,
            'to': yesterday
        }
        delivery_statistics = get_message_delivery_statistics(params_1)
        if delivery_statistics:
            app_df = pd.DataFrame()
            app_df['record_date'] = [str(date_now)]
            app_df['collection_date'] = [str(collection_date)]
            app_df['customAggregationUnit'] = [str(i)]
            if delivery_statistics['overview']:
                app_df['uniqueImpression'] = [str(delivery_statistics['overview']['uniqueImpression'])]
                app_df['uniqueClick'] = [str(delivery_statistics['overview']['uniqueClick'])]
                app_df['uniqueMediaPlayed'] = [str(delivery_statistics['overview']['uniqueMediaPlayed'])]
                app_df['uniqueMediaPlayed100Percent'] = [str(delivery_statistics['overview']['uniqueMediaPlayed100Percent'])]
            else:
                app_df['uniqueImpression'] = "None"
                app_df['uniqueClick'] = "None"
                app_df['uniqueMediaPlayed'] = "None"
                app_df['uniqueMediaPlayed100Percent'] = "None"

            if len(delivery_statistics['messages'])>0:
                app_df['impression'] = [str(delivery_statistics['messages'][0]['impression'])]
                app_df['mediaPlayed'] = [str(delivery_statistics['messages'][0]['mediaPlayed'])]
            else:
                app_df['impression'] = None
                app_df['mediaPlayed'] = None
                print(i, "No messages")
            if len(delivery_statistics['clicks'])>0:
                app_df['url_1'] = [str(delivery_statistics['clicks'][0]['url'])]
                app_df['url_1_click'] = [str(delivery_statistics['clicks'][0]['click'])]
                app_df['url_1_uniqueClick'] = [str(delivery_statistics['clicks'][0]['uniqueClick'])]
                app_df['url_1_uniqueClickOfRequest'] = [str(delivery_statistics['clicks'][0]['uniqueClickOfRequest'])]
            else:
                app_df['url_1'] = "None"
                app_df['url_1_click'] = "None"
                app_df['url_1_uniqueClick'] = "None"
                app_df['url_1_uniqueClickOfRequest'] = "None"
            if len(delivery_statistics['clicks'])>1:
                app_df['url_2'] = [str(delivery_statistics['clicks'][1]['url'])]
                app_df['url_2_click'] = [str(delivery_statistics['clicks'][1]['click'])]
                app_df['url_2_uniqueClick'] = [str(delivery_statistics['clicks'][1]['uniqueClick'])]
                app_df['url_2_uniqueClickOfRequest'] = [str(delivery_statistics['clicks'][1]['uniqueClickOfRequest'])]
            else:
                app_df['url_2'] = "None"
                app_df['url_2_click'] = "None"
                app_df['url_2_uniqueClick'] = "None"
                app_df['url_2_uniqueClickOfRequest'] = "None"
            if len(delivery_statistics['clicks'])>2:
                app_df['url_3'] = [str(delivery_statistics['clicks'][2]['url'])]
                app_df['url_3_click'] = [str(delivery_statistics['clicks'][2]['click'])]
                app_df['url_3_uniqueClick'] = [str(delivery_statistics['clicks'][2]['uniqueClick'])]
                app_df['url_3_uniqueClickOfRequest'] = [str(delivery_statistics['clicks'][2]['uniqueClickOfRequest'])]
            else:
                app_df['url_3'] = "None"
                app_df['url_3_click'] = "None"
                app_df['url_3_uniqueClick'] = "None"
                app_df['url_3_uniqueClickOfRequest'] = "None"
            if len(delivery_statistics['clicks'])>3:
                app_df['url_4'] = [str(delivery_statistics['clicks'][3]['url'])]
                app_df['url_4_click'] = [str(delivery_statistics['clicks'][3]['click'])]
                app_df['url_4_uniqueClick'] = [str(delivery_statistics['clicks'][3]['uniqueClick'])]
                app_df['url_4_uniqueClickOfRequest'] = [str(delivery_statistics['clicks'][3]['uniqueClickOfRequest'])]
            else:
                app_df['url_4'] = "None"
                app_df['url_4_click'] = "None"
                app_df['url_4_uniqueClick'] = "None"
                app_df['url_4_uniqueClickOfRequest'] = "None"            
            if len(delivery_statistics['clicks'])>4:
                app_df['url_5'] = [str(delivery_statistics['clicks'][4]['url'])]
                app_df['url_5_click'] = [str(delivery_statistics['clicks'][4]['click'])]
                app_df['url_5_uniqueClick'] = [str(delivery_statistics['clicks'][4]['uniqueClick'])]
                app_df['url_5_uniqueClickOfRequest'] = [str(delivery_statistics['clicks'][4]['uniqueClickOfRequest'])]
            else:
                app_df['url_5'] = "None"
                app_df['url_5_click'] = "None"
                app_df['url_5_uniqueClick'] = "None"
                app_df['url_5_uniqueClickOfRequest'] = "None"
            # print(app_df)
            final_df = pd.concat([final_df, app_df], ignore_index=True)
        else:
            print("Failed to retrieve statistics.")
    final_df.replace("None",np.nan,inplace=True)  
    final_df = final_df.replace({np.NAN: None})
    data = final_df.to_dict('records')
    try:
      insert_line_statistical_data(data, "foodpanda-th-bigquery.pandata_th_external.line_statistical_data_vendors")
    except BaseException as e:
      print(e)
      requests.post(slack_webhook,
      json = {'text' : '*line_statistiacal_data_collection*: Failed to record line statistical data: ' + str(e)})

