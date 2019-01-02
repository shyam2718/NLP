import  requests
import json

# TODO: replace with your own app_id and app_key
app_id = '87d6621d'
app_key = '086226e56a258a8179ccf5adc8b8071e'
language = 'en'
word_id = 'wipe'

url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower() + '/synonyms'
#url Normalized frequency
# urlFR = 'https://od-api.oxforddictionaries.com:443/api/v1/stats/frequency/word/'  + language + '/?corpus=nmc&lemma=' + '/synonyms'

r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})

# print("text \n" + r.text)
# syn = json.dumps(r.json())

t1 = json.loads(r.text)
ss = t1.get('synonyms')

print(ss)