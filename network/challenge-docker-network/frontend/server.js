'use strict';

const express = require('express');
const axios = require('axios');
var aes256 = require('aes256');

// Constants
const PORT = 80;
const HOST = '0.0.0.0';
const cipher = "5dLLNA8lovIG2hBkN8slok9mBfQ78ZKEYtLv08JVB/oSwZhx0WVuU8SbbuvYx6KFUA=="

// App
const app = express();
app.get('/flag', async (req, res) => {

    axios.get('http://backend:8080/secret')
        .then( async (response) => { // Fix occurred here
            let key = response.data;
            let flag = aes256.decrypt(key, cipher);
            res.send(flag);
        })
        .catch(err => {
            // Handle Error Here
            res.send("Can't find backend");
        });
});

app.listen(PORT, HOST);