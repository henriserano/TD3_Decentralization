document.getElementById("predictButton").addEventListener("click", function() {
    fetch('/predict')
        .then(response => response.json())
        .then(data => {
            document.getElementById("predictionResult").innerHTML = "Résultat de prédiction: " + data.prediction;
        })
        .catch(error => {
            console.error('Erreur lors de la récupération des prédictions:', error);
            document.getElementById("predictionResult").innerHTML = "Erreur lors de la récupération des prédictions.";
        });
});
