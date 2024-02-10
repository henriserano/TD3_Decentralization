import requests
import json

def get_consensus_prediction(data, model_urls):
    predictions = []
    for i in data:
        response = requests.post(model_urls, json=i)
        print(response.json())
        if response.json()['result'] == "Survivant":
            predictions.append(1)   
        else:
            predictions.append(0)
    consensus_prediction = sum(predictions) / len(predictions)
    return consensus_prediction

#OUR URL FROM NGROCK
model_urls = 'https://ostrich-driven-duly.ngrok-free.app/predict'  # Example URLs
data = [{'Pclass': '1', 'Sex': 'male', 'Age': '15', 'SibSp': '1', 'Parch': '3', 'Fare': '3', 'Embarked': 'C', 'algo': 'ml'},{'Pclass': '1', 'Sex': 'male', 'Age': '15', 'SibSp': '1', 'Parch': '3', 'Fare': '3', 'Embarked': 'C', 'algo': 'linear'},{'Pclass': '1', 'Sex': 'male', 'Age': '15', 'SibSp': '1', 'Parch': '3', 'Fare': '3', 'Embarked': 'C', 'algo': 'logic'}]
consensus_prediction = get_consensus_prediction(data, model_urls)
print(f"Consensus Prediction: {consensus_prediction}")


#Question 4 et 5
models = {
    "model1": {"weight": 1.0, "balance": 1000},
    "model2": {"weight": 1.0, "balance": 1000},
}

def update_model_performance(model_id, accuracy_delta):
    models[model_id]['weight'] += accuracy_delta  # Update weight based on performance
    if accuracy_delta < 0:  # Apply slashing if performance decreased
        models[model_id]['balance'] -= 100  # Example penalty
    
    # Ensure weights and balances don't go out of bounds
    models[model_id]['weight'] = min(max(models[model_id]['weight'], 0), 1)
    models[model_id]['balance'] = max(models[model_id]['balance'], 0)

    save_models_to_db(models)

def save_models_to_db(models):
    with open('models.json', 'w') as f:
        json.dump(models, f)

def load_models_from_db():
    with open('models.json', 'r') as f:
        return json.load(f)

models = load_models_from_db()  # Load existing data
update_model_performance('model1', -0.1)  # Example update
