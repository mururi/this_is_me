from . import main
import urllib.request, json
from .models import Quote

base_url = None

def configure_request(app):
    global base_url
    base_url = app.config['QUOTE_API_BASE_URL']

def get_quote():
    '''
    Function that gets the JSON response to our URL request
    '''

    with urllib.request.urlopen(base_url) as url:
        get_quote_data = url.read()
        get_quote_response = json.loads(get_quote_data)

        quote_results = None

        if get_quote_response['author']:
            quote_results = process_results(get_quote_response)

    return quote_results

def process_results(quote_object):
    author = quote_object.get('author')
    id = quote_object.get('id')
    quote = quote_object.get('quote')

    quote_results = Quote(author, id, quote)

    return quote_results