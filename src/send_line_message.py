import requests
import datetime
import json
import re

def send_request_line_api(url, headers, json, list):
    reponse_code_list = []
    url_list = []
    for i in list:
        user_specific_url = url.replace("user_id_variable", i)
        headers = headers
        json = json
        r = requests.post(user_specific_url, headers = headers, json = json)
        reponse_code = r.status_code
        reponse = r.json()
        reponse_code_list.append(reponse_code)
        url_list.append(user_specific_url)
    return reponse_code_list, url_list 

def send_request_line_api_v2(url, headers, json_data, list):
    reponse_code_list = []
    json_list = []
    for i in list:
        user_specific_url = url
        headers = headers
        json_data['to'] = i
        json = json_data
        r = requests.post(user_specific_url, headers = headers, json = json)
        reponse_code = r.status_code
        reponse = r.json()
        print(reponse)
        reponse_code_list.append(reponse_code)
        json_list_data = str(json)
        json_list.append(json_list_data)
    return reponse_code_list, json_list

def send_request_line_api_v3(*args, **kwargs):
    # reponse collections lists
    reponse_code_list = []
    json_list = []
    
    # setting variables
    url = kwargs['url']
    headers = kwargs['headers']
    json_string = kwargs['json_object']
    df = kwargs['dataframe']
    df.replace(to_replace=[None], value="No Value", inplace=True)
    df = df.reset_index() 
    for index, row in df.iterrows():
        json_data_v1 = json_string.replace('{LineUserID}', row['LineUserID']) \
                                .replace('{vendor_name}', row['vendor_name']) \
                                .replace('{vendor_code}', row['vendor_code']) \
                                .replace('{ihs_score}', row['ihs_score']) \
                                .replace('{customers}', row['customers']) \
                                .replace('{perc_customer_growth}', row['perc_customer_growth']) \
                                .replace('{valid_orders}', row['valid_orders']) \
                                .replace('{perc_order_growth}', row['perc_order_growth']) \
                                .replace('{top1_best_seller}', row['top1_best_seller']) \
                                .replace('{top2_best_seller}', row['top2_best_seller']) \
                                .replace('{top3_best_seller}', row['top3_best_seller']) \
                                .replace('{failed_orders}', row['failed_orders']) \
                                .replace('{improve_order}', row['improve_order']) \
                                .replace('{top_failed_product}', row['top_failed_product']) \
                                .replace('{improve_menu}', row['improve_menu']) \
                                .replace('{top_failed_reason}', row['top_failed_reason']) \
                                .replace('{improve_top_failed_reason}', row['improve_top_failed_reason']) \
                                .replace('{perc_offline}', row['perc_offline']) \
                                .replace('{top_offline_reason}', row['top_offline_reason']) \
                                .replace('{improve_top_offline_reason}', row['improve_top_offline_reason']) \
                                .replace('{first_date}', row['first_date']) \
                                .replace('{last_date}', row['last_date']) 
                   
        r = requests.post(url, headers = headers, data = json_data_v1.encode('utf-8'))
        reponse_code = r.status_code
        reponse_code_list.append(reponse_code)
        json_list.append(json_data_v1)
    return reponse_code_list, json_list 
