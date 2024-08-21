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

    // Send preferences to your backend (replace '/api/recommendations' with your API endpoint)
    const response = await fetch('/api/recommendations', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(preferences),
    });

    const recommendations = await response.json();

    // Store recommendations in localStorage
    localStorage.setItem('recommendations', JSON.stringify(recommendations));

    // Redirect to results page
    window.location.href = 'results.html';
});
