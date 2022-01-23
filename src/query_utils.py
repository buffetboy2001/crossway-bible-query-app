import requests
import json
import re

global API_KEY
API_URL = 'https://api.esv.org/v3/passage/text/'

def process_secrets(secrets_file:str=None):
    with open(secrets_file) as file:
        secrets_contents = json.load(file)

        global API_KEY
        API_KEY = secrets_contents['token']

def create_passage_query(book:str=None, chapter:str=None, verse:str=None):
    '''
    '''
    return f'{book} {chapter}:{verse}'


def get_esv_text(passage):
    params = {
        'q': passage,
        'indent-poetry': False,
        'include-headings': False,
        'include-footnotes': False,
        'include-verse-numbers': False,
        'include-short-copyright': False,
        'include-passage-references': False
    }

    headers = {
        'Authorization': 'Token %s' % API_KEY
    }

    data = requests.get(API_URL, params=params, headers=headers).json()

    text = re.sub('\s+', ' ', data['passages'][0]).strip()

    return text, data['canonical'] 

