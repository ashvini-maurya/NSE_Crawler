#!/usr/bin/python
import requests
import json
#from redis_storage import *

def gainers_or_losers(request_url):
        gainers_or_losers_req = requests.get(request_url)
        response_data = gainers_or_losers_req.json()
        #return response_data['data']
        return gainers_or_losers_req.text






#print redis_data_store('https://www.nseindia.com/live_market/dynaContent/live_analysis/gainers/niftyGainers1.json')
#print redis_data_store('https://www.nseindia.com/live_market/dynaContent/live_analysis/losers/niftyLosers1.json')


gainers_or_losers('https://www.nseindia.com/live_market/dynaContent/live_analysis/gainers/niftyGainers1.json')
gainers_or_losers('https://www.nseindia.com/live_market/dynaContent/live_analysis/losers/niftyLosers1.json')
