from flask import Flask, render_template, jsonify, request
from mlalgo import ml, linear, logic
import numpy as np
import json
import random

def load_model_data():
    with open('weight.json') as f:
        return json.load(f)

def save_model_data(data):
    with open('weight.json', 'w') as f:
        json.dump(data, f, indent=4)

def adjust_balance_and_weight(model_id, accurate):
    data = load_model_data()
    if accurate:
        data['models'][model_id]['weight'] *= 1.05
    else:
        data['models'][model_id]['balance'] -= 100
        data['models'][model_id]['weight'] *= 0.95
    save_model_data(data)

def simulate_accuracy_check(model_id):
    data = load_model_data()
    weight = data['models'][model_id]['weight']
    accuracy_chance = 0.5 + (weight - 1.0) * 0.1
    accuracy_chance = min(max(accuracy_chance, 0.1), 0.9) 
    return random.random() < accuracy_chance

app = Flask(__name__)

def convert_numpy(obj):
    if isinstance(obj, np.generic):
        return obj.item()
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
    print("Data : ", data)
    algo = data.pop('algo', None)
    
    if algo not in ['ml', 'linear', 'logic']:
        return jsonify({'error': 'Invalid algorithm selected'}), 400

    accurate = simulate_accuracy_check(algo)
    adjust_balance_and_weight(algo, accurate)

    if algo == 'ml':
        prediction = ml(data)
    elif algo == 'linear':
        prediction = linear(data)
    elif algo == 'logic':
        prediction = logic(data)

    result = "Survivant" if prediction == 1 else "Non survivant"
    
    return jsonify({'result': convert_numpy(result)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
