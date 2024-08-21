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

    console.log("User Preferences:", preferences); // For debugging

    // Hardcoded dataset for demonstration purposes
    const dataset = [
        { City: "Austin", State: "TX", CostOfLiving: 0.6, MedianIncome: 0.8, Population: 0.7, Education: 0.85, Safety: 0.75, TempWinter: 0.5, TempSpring: 0.8, TempSummer: 0.9, TempFall: 0.7 },
        { City: "Fargo", State: "ND", CostOfLiving: 0.7, MedianIncome: 0.75, Population: 0.4, Education: 0.8, Safety: 0.9, TempWinter: 0.3, TempSpring: 0.7, TempSummer: 0.8, TempFall: 0.6 },
        // Add more cities as needed
    ];

    // Function to calculate recommendation score
    function calculateScore(city, preferences) {
        let score = 0;

        // Adjust based on user preferences
        if (preferences.cost_of_living === 'high') score += city.CostOfLiving;
        if (preferences.median_income === 'high') score += city.MedianIncome;
        if (preferences.population === 'high') score += city.Population;
        if (preferences.education === 'high') score += city.Education;
        if (preferences.safety === 'high') score += city.Safety;
        if (preferences.winter_temp === 'warm') score += city.TempWinter;
        if (preferences.spring_temp === 'warm') score += city.TempSpring;
        if (preferences.summer_temp === 'warm') score += city.TempSummer;
        if (preferences.fall_temp === 'warm') score += city.TempFall;

        return score;
    }

    // Calculate recommendations
    const recommendations = dataset.map(city => ({
        ...city,
        recommendation_score: calculateScore(city, preferences)
    }));

    // Sort recommendations by score (descending)
    recommendations.sort((a, b) => b.recommendation_score - a.recommendation_score);

    console.log("Recommendations:", recommendations);

    // Store recommendations in localStorage
    localStorage.setItem('recommendations', JSON.stringify(recommendations));

    // Redirect to results page
    window.location.href = 'results.html';
});
