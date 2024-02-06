from flask import Flask, render_template, request, jsonify
from mlalgo import TitanicModel

app = Flask(__name__)

# Initialiser et entraîner le modèle au démarrage de l'app
tm = TitanicModel()
df = tm.load_data('titanic.csv')
df = tm.preprocess_data(df)
tm.train(df)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extraction des données du formulaire
    input_data = request.json
    prediction = tm.predict(input_data)
    result = "Survived" if prediction == 1 else "Did Not Survive"
    return jsonify({'prediction': result})

if __name__ == "__main__":
    app.run(debug=True)
