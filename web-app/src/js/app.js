document.getElementById('preferences-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    
    // Capture user preferences
    const costOfLiving = document.getElementById('cost_of_living').value;
    // Repeat for other preferences (income, population, education, safety, temperature)

    // Create a preferences object
    const preferences = {
        cost_of_living_weight: costOfLiving,
        // Add other preferences similarly
    };

    // Send preferences to your backend (replace with your API endpoint)
    const response = await fetch('/api/recommendations', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(preferences),
    });

    const recommendations = await response.json();
    
    // Display recommendations
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = recommendations.map(rec => `
        <div>
            <h3>${rec.City}, ${rec.State}</h3>
            <p>Score: ${rec.recommendation_score.toFixed(2)}</p>
        </div>
    `).join('');
});
