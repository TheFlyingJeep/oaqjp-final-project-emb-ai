''' Initiate the emotion detection application to be
    executed over the flask channel and deployed on
    localhost:5000
'''

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route('/emotionDetector')
def emote_detector():
    '''
        This code receives text from the HTML input
        and runs emotional detection on it using emotion_detector.
        The output returned shows the percentage of all emotions
        and the dominant emotion.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if not response['dominant_emotion']:
        return 'Invalid Input!'
    return f"For the given statement, the system response is \'anger\': \
    {response['anger']}, \'disgust\': {response['disgust']}, \'fear\': \
    {response['fear']}, \'joy\': {response['joy']}, \'sadness\': \
    {response['sadness']}. The dominant emotion is \
    {response['dominant_emotion']}"

@app.route('/')
def render_index():
    '''
        Renders the index.html file.
    '''
    return render_template("index.html")

if __name__ == "__MAIN__":
    app.run(host="0.0.0.0", port=5000)
