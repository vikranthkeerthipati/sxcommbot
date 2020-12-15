import requests 
import json
import os

def send(req_headers,req_body,filename):
    #Posts it through webhook
    res = requests.post(os.getenv("webhook"),data=json.dumps(req_body),headers=req_headers)
    print(res.json)

    #Moves file to past analytics to prevent clutter
    os.rename(os.path.abspath(os.getcwd())+"/"+filename, os.path.abspath(os.getcwd())+"/past_analytics/"+filename)