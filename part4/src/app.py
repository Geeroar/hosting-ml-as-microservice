from flask import Flask, request
from predict_sentiment_analysis import get_sentiment

app = Flask(__name__)

@app.route('/predict', methods = ['GET', 'POST'])
def predict():
    if request.method == 'GET':
        review = request.args.get('review')
    else:
        review = request.get_json(force=True)['review']
    if not review:
        return 'No review found'
    return get_sentiment(review)
