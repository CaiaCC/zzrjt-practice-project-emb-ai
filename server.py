from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    text_to_analyse = request.args.get('textToAnalyze')
    if len(text_to_analyze) == 0:
        return "Please enter a text to analyze"
    
    response = sentiment_analyzer(text_to_analyse)
    label = response['label']
    score = response['score']

    if label is None:
        return "Invalid input! Try again."

    return f"The given text has been identified as {label.split('_')[-1]} with a score of {score}."

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
