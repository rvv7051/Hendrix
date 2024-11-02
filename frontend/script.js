// Select the form element
const form = document.getElementById('myForm');

// Add an event listener for the form submission
form.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Get the value of the text input
    const nameInput = document.getElementById('name').value;
    const response = fetch('http://127.0.0.1:5000/api/test'); // Adjust URL based on your backend
    const data = response.json();

    // Display the input in the result paragraph
    document.getElementById('result').innerText = `Hello, ${nameInput}, ${data}`;

    // You can also call other functions here if needed
    // someFunction(nameInput);
});

async function fetchData() {
    try {
        //const response = await fetch('http://127.0.0.1:5000/api/test'); // Adjust URL based on your backend
        //console.log(response);
        const data = await response.json();
        document.getElementById('body').innerText = "hello wolrd";
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

function updateContent() {
    const title = document.getElementById("title");
    title.innerText = "Updated Title";

    const content = document.getElementById("content");
    content.textContent = "This is the updated content.";
}


//JSON.stringify(data, null, 2);