
window.onload = () => {
  const userData = localStorage.getItem("data");
  if (userData) {
    
      window.location.replace('./mi-perfil.html');

  }
};

const signButton = document.getElementById("sign-btn");


async function createUser(){
  let form = document.querySelector("form");
  let nameUser = document.getElementById("name-input").value;
  let emailUser = document.getElementById("email-input").value;
  let passwordUser = document.getElementById("password-input").value;
  let addressUser = document.getElementById("address-input").value;

  if (!nameUser || !emailUser || !passwordUser || !addressUser) {
    document.getElementById("error").innerHTML = "*Please complete all fields.";
    return;
  }
  const data={
    name: nameUser,
    data: {
      email: emailUser,
      password: passwordUser,
      address: addressUser
    }
  }
  try {
 
    const response = await axios.post("https://api.restful-api.dev/objects", data);

    alert("User created successfully! Your ID is: "+ response.data.id);
    localStorage.setItem("data", JSON.stringify(response.data)); 
    
    form.reset();
    location.href =  "./mi-perfil.html";
  } catch (error) {
    document.getElementById("error").innerHTML = `❌ An error occurred: ${error.message}. Please try again.`;



  }
}


signButton.addEventListener("click", createUser)
 

   
   