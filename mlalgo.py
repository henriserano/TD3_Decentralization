import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Chargement et préparation des données
df = pd.read_csv('titanic.csv')

imputer = SimpleImputer(strategy='mean')
df['Age'] = imputer.fit_transform(df[['Age']])
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

label_encoder = LabelEncoder()
df['Sex'] = label_encoder.fit_transform(df['Sex'])
df['Embarked'] = label_encoder.fit_transform(df['Embarked'])

features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
X = df[features]
y = df['Survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fonction pour préparer les données d'entrée utilisateur
def prepare_input_data(data):
    # Convertit les données d'entrée en DataFrame
    input_data = pd.DataFrame([data])
    print(input_data)
    # Appliquer les transformations nécessaires ici, par exemple:
    sex_mapping = {'male': 1, 'female': 0}
    input_data['Sex'] = input_data['Sex'].map(sex_mapping)
    
    # Pour 'Embarked', vous devez utiliser l'encodage basé sur le LabelEncoder utilisé lors de l'entraînement
    # Exemple simplifié, adapté selon votre cas
    embarked_mapping = {'S': 0, 'C': 1, 'Q': 2}
    input_data['Embarked'] = input_data['Embarked'].map(lambda x: embarked_mapping.get(x, -1))  # Utilise -1 pour les valeurs inconnues
    
    # Assurez-vous que le reste des colonnes est traité correctement
    # Exemple: Imputation, etc.
    
    return input_data

# RANDOM FOREST ALGORITHM
def ml(data):
    input_data = prepare_input_data(data)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    predictions = model.predict(input_data)
    print("Ma prédiction celon l'algo random forest : ",predictions)
    return predictions[0]  # Retourne la prédiction pour l'entrée utilisateur

# LINEAR REGRESSION ALGORITHM
def linear(data):
    input_data = prepare_input_data(data)
    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(input_data)
    print("Ma prédiction celon Linear regression : ",predictions)
    return round(predictions[0])  # Retourne la prédiction arrondie pour l'entrée utilisateur

# LOGISTIC REGRESSION ALGORITHM
def logic(data):
    input_data = prepare_input_data(data)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(input_data)
    print("Ma prediction celon la logic regression : ",predictions)
    return predictions[0]  # Retourne la prédiction pour l'entrée utilisateur
