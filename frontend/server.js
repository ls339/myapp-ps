const express = require('express');
const axios = require('axios');
const app = express();

const BACKEND_URL = process.env.BACKEND_URL + '/api/strings';

app.get('/', async (req, res) => {
  res.redirect('/api/display');
});

app.get('/api/display', async (req, res) => {
  try {
    const response = await axios.get(BACKEND_URL);
    // A cheat since we know there is only one value returned.
    res.send(response.data[0]["string_value"]);
  } catch (error) {
    res.status(500).send('Error fetching string.');
  }
});

app.listen(8080, () => {
  console.log('Frontend service running on port 8080');
});
