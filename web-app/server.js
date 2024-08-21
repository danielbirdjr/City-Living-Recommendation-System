const express = require('express');
const bodyParser = require('body-parser');
const csv = require('csv-parser');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(bodyParser.json());

app.post('/api/recommendations', (req, res) => {
    // Your existing code to handle the recommendations logic
    res.status(200).json({ message: "POST request received" }); // Temporary response for testing
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
