// JavaScript to handle button selections
document.querySelectorAll('.answers').forEach(answerGroup => {
    answerGroup.addEventListener('click', function(e) {
        if (e.target.tagName === 'BUTTON') {
            // Deselect any other buttons in the same group
            this.querySelectorAll('button').forEach(button => {
                button.classList.remove('selected');
            });
            // Select the clicked button
            e.target.classList.add('selected');
        }
    });
});

// Handle form submission and send data to the backend
document.querySelector('.submit_button').addEventListener('click', async function() {
    const preferences = {};
    document.querySelectorAll('.answers').forEach(answerGroup => {
        const question = answerGroup.getAttribute('data-question');
        const selectedButton = answerGroup.querySelector('.selected');
        if (selectedButton) {
            const value = selectedButton.getAttribute('data-value');
            preferences[question] = value;
        }
    });

    console.log(preferences); // Check if preferences are being captured correctly

    // Send preferences to your backend (replace '/api/recommendations' with your API endpoint)
    const response = await fetch('/api/recommendations', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(preferences),
    });

    const recommendations = await response.json();

    window.location.href = '/results.html'; // Redirect to results page

    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = recommendations.map(rec => `
        <div>
            <h3>${rec.City}, ${rec.State}</h3>
            <p>Score: ${rec.recommendation_score.toFixed(2)}</p>
        </div>
    `).join('');
});
