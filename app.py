from flask import Flask, render_template, jsonify
from mlalgo import ml
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict')
def predict():
    prediction = predict()
    return jsonify({'prediction': prediction})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
