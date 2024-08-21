const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');

export default function handler(req, res) {
    if (req.method !== 'POST') {
        res.status(405).json({ message: 'Only POST requests are allowed' });
        return;
    }

    const preferences = req.body;

    // Define the path to the Python script
    const pythonScriptPath = path.join(process.cwd(), 'src', 'analysis', 'recommendation_system.py');

    // Spawn a new process to run the Python script
    const pythonProcess = spawn('python3', [pythonScriptPath, JSON.stringify(preferences)]);

    let dataToSend = '';

    pythonProcess.stdout.on('data', (data) => {
        dataToSend += data.toString();
    });

    pythonProcess.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
    });

    pythonProcess.on('close', (code) => {
        if (code !== 0) {
            res.status(500).json({ message: 'Error in processing recommendations' });
            return;
        }

        try {
            const recommendations = JSON.parse(dataToSend);
            res.status(200).json(recommendations);
        } catch (error) {
            res.status(500).json({ message: 'Error parsing recommendation results' });
        }
    });
}
