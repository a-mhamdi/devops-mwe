require("dotenv").config();

const express = require("express");
const path = require("path");

const app = express();

app.use(
  express.static(path.join(__dirname, "public")),
  express.static(path.join(__dirname, "js")),
);

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "index.html"));
});

const API_URL = process.env.BACKEND_URL;
console.log(API_URL);

app.get("/config.js", (req, res) => {
  res.type("application/javascript");
  res.send(`
    window.CONFIG = {
      API_URL: "${API_URL}"
    };
  `);
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`MWE listening on port ${PORT}`);
});
