const express = require('express');
const axios = require('axios');
const app = express();

const BACKEND_URL = process.env.BACKEND_URL + '/api/strings';

app.get('/api/display', async (req, res) => {
  try {
    const response = await axios.get(BACKEND_URL);
    res.json(response.data);
  } catch (error) {
    res.status(500).send('Error fetching string.');
  }
});

app.listen(8080, () => {
  console.log('Frontend service running on port 8080');
});
