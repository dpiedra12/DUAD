window.onload = () => {
    const userData = localStorage.getItem("data");
    if (!userData) {
      document.body.innerHTML = "<h1>Redirecting to Sign in...</h1>";
      setTimeout(() => {
        location.href = "./login.html";
      }, 500); 
    }
  };
  

const signButton = document.getElementById("sign-btn");

async function getInfo(){

    try {
        const userData = JSON.parse(localStorage.getItem('data'));
        const userID = userData.id;
     
        if (userID) {
            const response = await axios.get(`https://api.restful-api.dev/objects/${userID}`);

            document.getElementById("user-id").innerHTML = `User ID: ${response.data.id}`;
            document.getElementById("name").innerHTML = `Name: ${response.data.name}`;
            document.getElementById("name").innerHTML = `Name: ${response.data.name}`;
            document.getElementById("email").innerHTML = `Email: ${response.data.data.email}`;
            const passwordSpan = document.getElementById("password");
            passwordSpan.setAttribute("data-password", response.data.data.password);
            passwordSpan.textContent = "******";
            document.getElementById("address").innerHTML = `Address: ${response.data.data.address}`;

            document.querySelector(".profile-container").style.display = "block";


        }
    } catch (error) {
        document.getElementById("error").innerHTML = `An error occurred: ${error.message}`;
    }
  
}
document.addEventListener("DOMContentLoaded", getInfo);

function togglePassword() {
    const passwordSpan = document.getElementById("password");
    if (passwordSpan.textContent === "******") {
        passwordSpan.textContent = passwordSpan.getAttribute("data-password");
    } else {
        passwordSpan.textContent = "******";
    }
}

signButton.addEventListener("click", () => {
    setTimeout(function() { 
        alert("You have successfully logged out."); 
        localStorage.clear();                         
        location.href = "./login.html"; 
    }, 700); 
});