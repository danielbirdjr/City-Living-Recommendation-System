const fs = require('fs');
const path = require('path');

export default function handler(req, res) {
    if (req.method !== 'POST') {
        res.status(405).json({ message: 'Only POST requests are allowed' });
        return;
    }

    const preferences = req.body;

    // Load your dataset
    const datasetPath = path.join(process.cwd(), 'data', 'everything_dataset.csv');
    const dataset = fs.readFileSync(datasetPath, 'utf-8');

    // Parse the CSV (for simplicity, you might want to use a library like papaparse)
    const rows = dataset.split('\n').slice(1); // Skip header row
    const cities = rows.map(row => {
        const [City, State, CostOfLiving, MedianIncome, Population, Education, Safety, TempWinter, TempSpring, TempSummer, TempFall] = row.split(',');
        return { City, State, CostOfLiving, MedianIncome, Population, Education, Safety, TempWinter, TempSpring, TempSummer, TempFall };
    });

    // Here, you'd calculate the recommendation_score based on user preferences
    const recommendations = cities.map(city => {
        let score = 0;

        if (preferences.cost_of_living === 'high') score += parseFloat(city.CostOfLiving);
        if (preferences.median_income === 'high') score += parseFloat(city.MedianIncome);
        if (preferences.population === 'high') score += parseFloat(city.Population);
        if (preferences.education === 'high') score += parseFloat(city.Education);
        if (preferences.safety === 'high') score += parseFloat(city.Safety);
        if (preferences.winter_temp === 'warm') score += parseFloat(city.TempWinter);
        if (preferences.spring_temp === 'warm') score += parseFloat(city.TempSpring);
        if (preferences.summer_temp === 'warm') score += parseFloat(city.TempSummer);
        if (preferences.fall_temp === 'warm') score += parseFloat(city.TempFall);

        return {
            City: city.City,
            State: city.State,
            recommendation_score: score
        };
    });

    // Sort recommendations by score (descending)
    recommendations.sort((a, b) => b.recommendation_score - a.recommendation_score);

    // Return the top 10 recommendations
    res.status(200).json(recommendations.slice(0, 10));
}
