import redis
from script import *
#import script

r = redis.StrictRedis(host='localhost', port=6379, db=0)


def redis_data_store(gainers_or_losers_request):
        list_of_dict = gainers_or_losers(gainers_or_losers_request)
        json_data = json.dumps(list_of_dict)
        new_json_data = json.dumps(json_data)
        r.set(list_of_dict, new_json_data)
        unpacked_data = json.loads(r.get(list_of_dict))
        list_of_dict == unpacked_data

        return list_of_dict



redis_data_store('https://www.nseindia.com/live_market/dynaContent/live_analysis/gainers/niftyGainers1.json')
redis_data_store('https://www.nseindia.com/live_market/dynaContent/live_analysis/losers/niftyLosers1.json')


