function loadMessage() {
    fetch("http://127.0.0.1:5000/hello")
        .then(response => response.json())
        .then(data => {
            document.getElementById("apiMessage").innerText = data.message;
        })
        .catch(error => {
            console.log(error)
            document.getElementById("apiMessage").innerText = "Error";
        });
}

loadMessage();