from predict_sentiment_analysis import get_sentiment, get_sentiment_batch

CORS_ORIGIN = 'https://storage.googleapis.com'

def predict_sentiment(request):
    if request.method == 'OPTIONS':
        headers = {
                'Access-Control-Allow-Origin': CORS_ORIGIN,
                'Access-Control-Allow-Methods': 'GET, POST',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Max-Age': '3600'
                }
        return ('', 204, headers)
    json = request.get_json()
    cors_header = {'Access-Control-Allow-Origin': CORS_ORIGIN}
    if not json:
        return ('Error! Request payload is not JSON', 400, cors_header)
    elif 'review' in json:
        return (str(get_sentiment(json['review'])), 200, cors_header)
    elif 'reviews' in json:
        return (str(get_sentiment_batch(json['reviews'])), 200, cors_header)
    else:
        return ('Error! No review found', 400, cors_header)
