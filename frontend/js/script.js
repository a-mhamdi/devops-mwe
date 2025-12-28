const API_URL = "http://localhost:8000";

async function getRoot() {
    alert("Fetching `/` endpoint!");
    fetch(API_URL)
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            document.getElementById("message").innerText =
                "Response from root endpoint: " + JSON.stringify(data.message);
        })
        .catch((error) => {
            console.error("Error fetching root endpoint:", error);
            document.getElementById("message").innerText =
                "Error fetching root endpoint: " + error;
        });
}

async function getItems() {
    alert("Fetching `get_items` endpoint!");
    fetch(API_URL + "/get_items")
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            document.getElementById("message").innerText =
                "Response from get_items endpoint: " + JSON.stringify(data);
        })
        .catch((error) => {
            console.error("Error fetching get_items endpoint:", error);
            document.getElementById("message").innerText =
                "Error fetching get_items endpoint: " + error;
        });
}

async function postItems() {
    alert("Posting to `set_items` endpoint!");

    const name = document.getElementById('name').value;
    const description = document.getElementById('description').value;
    const price = document.getElementById('price').value;
    const tax = document.getElementById('tax').value;


    fetch(API_URL + "/set_items", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ 
            name: name, 
            description: description, 
            price: price, 
            tax: tax
        }),
    })
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            document.getElementById("message").innerText =
                "Response from set_items endpoint: " + JSON.stringify(data);
        })
        .catch((error) => {
            console.error("Error posting to set_items endpoint:", error);
            document.getElementById("message").innerText =
                "Error posting to set_items endpoint: " + error;
        });
}
