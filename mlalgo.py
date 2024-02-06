import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
global df
df = pd.read_csv('titanic.csv') 

def ml():
    imputer = SimpleImputer(strategy='mean')
    df['Age'] = imputer.fit_transform(df[['Age']])
    df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

    # Encodage des variables catégorielles
    label_encoder = LabelEncoder()
    df['Sex'] = label_encoder.fit_transform(df['Sex'])
    df['Embarked'] = label_encoder.fit_transform(df['Embarked'])

    # Sélection des colonnes à utiliser pour l'apprentissage
    features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
    X = df[features]
    y = df['Survived']

    # 3. Séparation des données
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 4. Création du modèle
    model = RandomForestClassifier(n_estimators=100, random_state=42)

    # 5. Entraînement du modèle
    model.fit(X_train, y_train)

    # 6. Évaluation du modèle
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy}")

    # 7. Prédictions (exemple)
    # Prédictions sur les premières instances de l'ensemble de test
    predictions = model.predict(X_test.head())
    print("Predictions:", predictions)

    # 8. Statistiques du modèle
    feature_importances = model.feature_importances_
    print("Feature importances:", feature_importances)
    return accuracy

def linear():
    # Prétraitement des données
    imputer = SimpleImputer(strategy='mean')
    df['Age'] = imputer.fit_transform(df[['Age']])
    df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

    # Encodage des variables catégorielles
    label_encoder = LabelEncoder()
    df['Sex'] = label_encoder.fit_transform(df['Sex'])
    df['Embarked'] = label_encoder.fit_transform(df['Embarked'])

    # Sélection des colonnes à utiliser pour l'apprentissage
    features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
    X = df[features]
    y = df['Survived']

    # Séparation des données
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Création du modèle de régression linéaire
    model = LinearRegression()

    # Entraînement du modèle
    model.fit(X_train, y_train)

    # Prédictions
    y_pred = model.predict(X_test)

    # Évaluation du modèle
    rounded_predictions = [round(pred) for pred in y_pred]
    accuracy = accuracy_score(y_test, rounded_predictions)
    print(f"Accuracy: {accuracy}")

    # Prédictions (exemple)
    rounded_example_predictions = [round(pred) for pred in model.predict(X_test.head())]
    print("Predictions:", rounded_example_predictions)

    # Statistiques du modèle (coefficients)
    coefficients = model.coef_
    intercept = model.intercept_
    print("Coefficients:", coefficients)
    print("Intercept:", intercept)
    return accuracy

def logistic(): 
    imputer = SimpleImputer(strategy='mean')
    df['Age'] = imputer.fit_transform(df[['Age']])
    df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

    # Encodage des variables catégorielles
    label_encoder = LabelEncoder()
    df['Sex'] = label_encoder.fit_transform(df['Sex'])
    df['Embarked'] = label_encoder.fit_transform(df['Embarked'])

    # Sélection des colonnes à utiliser pour l'apprentissage
    features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
    X = df[features]
    y = df['Survived']

    # Séparation des données
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Création du modèle de régression logistique
    model = LogisticRegression()

    # Entraînement du modèle
    model.fit(X_train, y_train)

    # Évaluation du modèle
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy}")

    # Prédictions (exemple)
    predictions = model.predict(X_test.head())
    print("Predictions:", predictions)

    # Statistiques du modèle (coefficients)
    coefficients = model.coef_
    intercept = model.intercept_
    print("Coefficients:", coefficients)
    print("Intercept:", intercept)
    return accuracy