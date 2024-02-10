from flask import Flask, render_template, jsonify, request
from mlalgo import ml, linear, logic
import numpy as np
app = Flask(__name__)

def convert_numpy(obj):
    if isinstance(obj, np.generic):
        return obj.item()  # Utilisez .item() pour convertir des scalaires Numpy
    elif isinstance(obj, dict):
        return {key: convert_numpy(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [convert_numpy(item) for item in obj]
    else:
        return obj


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    print("Data : ",data)
    algo = data.pop('algo', None)  # Extrait l'algo choisi et retire 'algo' des données
    
    if algo == 'ml':
        prediction = ml(data)
    elif algo == 'linear':
        prediction = linear(data)
    elif algo == 'logic':
        prediction = logic(data)
    else:
        return jsonify({'error': 'Invalid algorithm selected'}), 400
    
    if prediction == 0:
        result = "Non survivant" 
    else:
        result = "Survivant"
    
    return jsonify({'result': convert_numpy(result)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)