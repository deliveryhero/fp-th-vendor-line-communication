import requests
import datetime

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


