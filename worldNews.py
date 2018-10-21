# Originally written by Harrison Sentdex
# Github: https://github.com/Sentdex
# Tutorial: https://pythonprogramming.net/intro-alexa-skill-flask-ask-python-tutorial/
#
#
# Edited Jordan Voss


import time
import json
import unidecode

def get_headlines(session):
    user_pass_dict = {'user': 'your_username',
                      'passwd': 'your_password',
                      'api_type': 'json'}
    sess = session
    sess.headers.update({'User-Agent': 'I am testing Alexa: Sentdex'})
    sess.post('https://www.reddit.com/api/login', data = user_pass_dict)
    time.sleep(1)
    url = 'https://reddit.com/r/worldnews/.json?limit=5'
    html = sess.get(url)
    data = json.loads(html.content.decode('utf-8'))
    titles = [unidecode.unidecode(listing['data']['title']) for listing in data['data']['children']]
    titles = '... '.join([i for i in titles])
	

    headline_msg = 'The current world news headlines are {}'.format(titles)
    return headline_msg 