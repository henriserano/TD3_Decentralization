from flask import Flask, render_template, jsonify
from mlalgo import ml, linear, logistic
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict')
def predict():
    prediction = str(predict())
    print(prediction)
    linearr = str(linear())
    print(linearr)
    logist = str(logistic()) 
    
    return jsonify({'prediction': prediction, 'linear': linearr, 'logistic': logist })

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
