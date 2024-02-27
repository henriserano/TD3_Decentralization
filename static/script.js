document.getElementById('predictButton').addEventListener('click', function() {
    const formData = new FormData(document.getElementById('predictionForm'));
    const data = {};
    formData.forEach((value, key) => {data[key] = value;});
    
    // Aucun besoin de corriger 'Sex' et 'Embarked' ici, cela devrait être géré côté serveur ou ajusté selon le besoin

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('predictionResult').innerText = 'Result: ' + data.result;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});

