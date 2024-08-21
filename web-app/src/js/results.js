document.addEventListener('DOMContentLoaded', () => {
    // This would be populated with data from the backend
    const recommendations = JSON.parse(localStorage.getItem('recommendations'));

    const resultsDiv = document.getElementById('results');
    
    if (recommendations && recommendations.length > 0) {
        resultsDiv.innerHTML = recommendations.map(rec => `
            <div>
                <h3>${rec.City}, ${rec.State}</h3>
                <p>Score: ${rec.recommendation_score.toFixed(2)}</p>
            </div>
        `).join('');
    } else {
        resultsDiv.innerHTML = '<p>No recommendations found.</p>';
    }
});
