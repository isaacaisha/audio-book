//function playSpeech() {
//    var audio = new Audio("data:audio/mp3;base64," + "{{ synthesized_text }}");
//    audio.play();
//}
//
//// Function to hide the error message
//function hideErrorMessage() {
//    var errorMessage = document.getElementById('error-message');
//    errorMessage.style.display = 'none';
//    errorMessage.innerText = ''; // Clear the text content
//}
//
//// Function to show the error message with specific text
//function showErrorMessage(text) {
//    var errorMessage = document.getElementById('error-message');
//    errorMessage.style.display = 'block';
//    errorMessage.innerText = text; // Set the text content
//}
//
//// Function to validate URL using a regular expression
//function isValidUrl(url) {
//    var urlPattern = /^(https?|ftp):\/\/[^\s/$.?#].[^\s]*$/;
//    return urlPattern.test(url);
//}
//
//// Hide the error message initially
//hideErrorMessage();
//
//// Handle form submission
//var form = document.querySelector('form');
//form.addEventListener('submit', function (event) {
//    var userInput = document.getElementById('userInput');
//    if (userInput.value.trim() === '') {
//        showErrorMessage("Please enter an URL."); // Set the error message text
//        event.preventDefault(); // Prevent form submission
//    } else if (!isValidUrl(userInput.value.trim())) {
//        showErrorMessage("Please enter a valid URL."); // Set the error message for an invalid URL
//        event.preventDefault(); // Prevent form submission
//    } else {
//        hideErrorMessage();
//    }
//});
//
//// Check conditions and show the error message if necessary when clicking the button
//var startButton = document.querySelector('[name="start"]');
//var userInput = document.getElementById('userInput');
//startButton.addEventListener('click', function () {
//    if (userInput.value.trim() === '') {
//        showErrorMessage("Please enter an URL."); // Set the error message text
//    } else if (!isValidUrl(userInput.value.trim())) {
//        showErrorMessage("Please enter a valid URL."); // Set the error message for an invalid URL
//    } else {
//        hideErrorMessage();
//    }
//});


// Add a click event listener to the button with the id "principito-button-1"
document.getElementById("principito-button-1").addEventListener("click", function() {
    // No need to prevent default behavior
    // Make a simple link to your Flask route
    window.location.href = "/el-p1";
});

// Add a click event listener to the button with the id "principito-button-2"
document.getElementById("principito-button-2").addEventListener("click", function() {
    // No need to prevent default behavior
    // Make a simple link to your Flask route
    window.location.href = "/el-p2";
});

// Add a click event listener to the button with the id "principito-button-3"
document.getElementById("principito-button-3").addEventListener("click", function() {
    // No need to prevent default behavior
    // Make a simple link to your Flask route
    window.location.href = "/el-p3";
});

// Add a click event listener to the button with the id "principito-button-4"
document.getElementById("principito-button-4").addEventListener("click", function() {
    // No need to prevent default behavior
    // Make a simple link to your Flask route
    window.location.href = "/el-p4";
});

// Add a click event listener to the button with the id "principito-button-5"
document.getElementById("principito-button-5").addEventListener("click", function() {
    // No need to prevent default behavior
    // Make a simple link to your Flask route
    window.location.href = "/el-p5";
});

// Add a click event listener to the button with the id "principito-button-6"
document.getElementById("principito-button-6").addEventListener("click", function() {
    // No need to prevent default behavior
    // Make a simple link to your Flask route
    window.location.href = "/el-p6";
});

// Add a click event listener to the button with the id "principito-button-7"
document.getElementById("principito-button-7").addEventListener("click", function() {
    // No need to prevent default behavior
    // Make a simple link to your Flask route
    window.location.href = "/el-p7";
});

// Add a click event listener to the button with the id "stella-button"
document.getElementById("stella-button").addEventListener("click", function() {
    // No need to prevent default behavior
    // Make a simple link to your Flask route for Stella
    window.location.href = "/stella-audio-book";
});

// Add a click event listener to the button with the id "les-miserables-button"
document.getElementById("les-miserables-button").addEventListener("click", function() {
    // No need to prevent default behavior
    // Make a simple link to your Flask route for Les Miserables
    window.location.href = "/les-m-book";
});
