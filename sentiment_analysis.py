import requests
import json

def sentiment_analyzer(text_to_analyse):
    URL = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    INPUT_JSON = { "raw_document": { "text": text_to_analyse } }
    HEADER = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    response = requests.post(URL, json = INPUT_JSON, headers=HEADER)
    formatted_response = json.load(response)

    return {
        'label': formatted_response['documentSentiment']['label'],
        'score': formatted_response['documentSentiment']['score']
    }