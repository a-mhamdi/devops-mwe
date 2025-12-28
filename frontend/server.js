const express = require('express');
const path = require('path');

const app = express();

app.use(express.static(path.join(__dirname, 'public')), express.static(path.join(__dirname, 'js')));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

const port = process.env.PORT || 3000;
app.listen(port, () => {
    console.log(`MWE listening on port ${port}`);
});
