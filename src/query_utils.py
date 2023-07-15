import requests
import json
import re
import time

global API_KEY
API_URL = 'https://api.esv.org/v3/passage/text/'

def process_secrets(secrets_file:str=None):
    with open(secrets_file) as file:
        secrets_contents = json.load(file)

        global API_KEY
        API_KEY = secrets_contents['token']

def create_passage_query(book:str=None, chapter:str=None, verse:str=None) -> str:
    """Create the query string.

    Args:
        book (str, required): Book of the Bible. Defaults to None.
        chapter (str, optional): Chapter of the book. Defaults to None.
        verse (str, optional): Verse of the chapter. Defaults to None.

    Returns:
        str: The query string, properly formatted.
    """
    if book is None:
        raise "Invalid query. Must provide 'book' at minimum."
    return f'{book} {chapter}:{verse}'


def get_esv_text(passage:str=None, params:dict=None) -> tuple:
    """Make the query. 

    Args:
        passage (str, requried): The passage to query for. Defaults to None. See also create_passage_query().
        params (dict, optional): Control over the returned query. Defaults to None which turns off all customizations.

    Returns:
        tuple: (requested text, canonical data)
    """
    if params is None:
        params = {
            'q': passage,
            'indent-poetry': False,
            'include-headings': False,
            'include-footnotes': False,
            'include-verse-numbers': False,
            'include-short-copyright': False,
            'include-passage-references': False
        }
    else:
        params['q'] = passage
    headers = {
        'Authorization': 'Token %s' % API_KEY
    }

    text = None
    data = requests.get(API_URL, params=params, headers=headers).json()
    if 'passages' in list(data.keys()):
        text = re.sub('\s+', ' ', data['passages'][0]).strip()

    if 'canonical' not in data.keys() and 'detail' in data.keys():
        if 'throttled' in str(data['detail']):
            # querying too fast...service is shutting us down...wait 30 seconds
            words = reversed(str(data['detail']).split())
            wait_duration = 30
            for word in words:
                if word.isnumeric():
                    wait_duration = int(word)
            time.sleep(wait_duration)
            return get_esv_text(passage=passage, params=params)
        else:
            print(f'Something unexpected occurred: {data["detail"]}')
    return text, data['canonical'] 

