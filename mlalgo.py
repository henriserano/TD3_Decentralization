import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
df = pd.read_csv('titanic.csv') 
# 2. Prétraitement des données
# Gestion des valeurs manquantes pour l'âge et le port d'embarquement
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
