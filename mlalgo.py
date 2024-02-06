import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder

class TitanicModel:
    def __init__(self):
        self.model = DecisionTreeClassifier(random_state=42)
        self.label_encoder_sex = LabelEncoder()
        self.label_encoder_embarked = LabelEncoder()
        self.imputer = SimpleImputer(strategy='mean')

    def load_data(self, filepath):
        df = pd.read_csv(filepath)
        return df

    def preprocess_data(self, df):
        # Gestion des valeurs manquantes
        df['Age'] = self.imputer.fit_transform(df[['Age']])
        df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

        # Encodage des variables catégorielles
        df['Sex'] = self.label_encoder_sex.fit_transform(df['Sex'])
        df['Embarked'] = self.label_encoder_embarked.fit_transform(df['Embarked'])

        return df

    def train(self, df):
        # Sélection des colonnes à utiliser pour l'apprentissage
        features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
        X = df[features]
        y = df['Survived']

        # Séparation des données
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Entraînement du modèle
        self.model.fit(X_train, y_train)

        # Évaluation du modèle
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Accuracy: {accuracy}")

    def predict(self, input_features):
        processed_features = self.preprocess_data(pd.DataFrame([input_features]))
        prediction = self.model.predict(processed_features)
        return prediction[0]

# Exemple d'utilisation
if __name__ == "__main__":
    tm = TitanicModel()
    df = tm.load_data('titanic.csv')
    df = tm.preprocess_data(df)
    tm.train(df)
    
    # Exemple de prédiction
    # Remplacer les valeurs ci-dessous par les entrées réelles pour la prédiction
    input_features = {'Pclass': 3, 'Sex': 'male', 'Age': 22, 'SibSp': 1, 'Parch': 0, 'Fare': 7.25, 'Embarked': 'S'}
    prediction = tm.predict(input_features)
    print(f"Predicted Survival: {prediction}")
