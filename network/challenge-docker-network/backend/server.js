'use strict';

const express = require('express');

// Constants
const PORT = 8080;
const HOST = '0.0.0.0';

// App
const app = express();
app.get('/secret', (req, res) => {
    res.send('super_secret_secret_4985328');
});

app.listen(PORT, HOST);