
document.getElementById('predictButton').addEventListener('click', function() {
    const formData = new FormData(document.getElementById('predictionForm'));
    const data = {};
    formData.forEach((value, key) => {data[key] = value;});

    // Correction pour l'encodage de 'Sex' et 'Embarked' si nécessaire
    data['Sex'] = data['Sex'].toLowerCase() === 'male' ? 1 : 0; // Assurez-vous que cela correspond à votre encodage
    data['Embarked'] = data['Embarked'].toUpperCase(); // 'C', 'Q', 'S'
    
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('predictionResult').innerText = 'Prediction: ' + data.prediction;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
