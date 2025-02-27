
window.onload = () => {
  const userData = localStorage.getItem("data");
  if (userData) {
     
      window.location.replace('./mi-perfil.html');

  }
};

const signButton = document.getElementById("sign-btn");


async function singinUser(userID,passwordUser ){
  let form = document.querySelector("form");
  
  try {
    
    const response = await axios.get(`https://api.restful-api.dev/objects/${userID}`);

    if (userID  === response.data.id && passwordUser === response.data.data.password ){
        localStorage.setItem("data", JSON.stringify(response.data)); 
        form.reset();
       location.href =  `./mi-perfil.html`;

    } else{
      document.getElementById("error").innerHTML = "Invalid credentials:  User ID or password";
    }

      
  } catch (error) {
    
    document.getElementById("error").innerHTML = "Invalid credentials:  User ID or password";
  

  }
}

signButton.addEventListener("click", () => {
    const userID = document.getElementById("userID-input").value;
    const passwordUser = document.getElementById("password-input").value;
    if (!userID || !passwordUser) {
      document.getElementById("error").innerHTML = "*User ID and password required.";
      return;
    }
    singinUser(userID, passwordUser);
   
    
  });

  const resetButton = document.getElementById("reset-btn");
  resetButton.addEventListener("click", () => {
   
    window.location.replace('./password-reset.html');
    
   
    
  });

 