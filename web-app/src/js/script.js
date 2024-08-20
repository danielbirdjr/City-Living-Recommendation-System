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

// Example of what you could do upon form submission
document.querySelector('.submit_button').addEventListener('click', function() {
    const preferences = {};
    document.querySelectorAll('.answers').forEach(answerGroup => {
        const question = answerGroup.getAttribute('data-question');
        const selectedButton = answerGroup.querySelector('.selected');
        if (selectedButton) {
            const value = selectedButton.getAttribute('data-value');
            preferences[question] = value;
        }
    });
    console.log(preferences); // You can handle form data here
});
