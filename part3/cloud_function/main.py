from predict_sentiment_analysis import get_sentiment, get_sentiment_batch

def predict_sentiment(request):
    json = request.get_json()
    if not json:
        return 'Error! Request payload is not JSON'
    elif 'review' in json:
        return get_sentiment(json['review'])
    elif 'reviews' in json:
        return str(get_sentiment_batch(json['reviews']))
    else:
        return 'Error! No review found'
