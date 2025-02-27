const passResetButton = document.getElementById("passreset-btn");

//Validate Fields
async function validateFields(userID, currentPassword,newPassword, confirmPassword){
  
  document.getElementById("error").innerHTML ="";
  
  try {
    
      const response = await axios.get(`https://api.restful-api.dev/objects/${userID}`);
  debugger;
    if (userID  !== response.data.id){

       document.getElementById("error").innerHTML = "❌ Error: User ID not found.";
       return false;
    } 

   else if(currentPassword !== response.data.data.password){
    document.getElementById("error").innerHTML = "❌ Error: Invalid current password.";
    return false;
    }

    else if(newPassword !== confirmPassword){
        document.getElementById("error").innerHTML = "❌ Error: New password and confirmation do not match.";
        return false;
    }



      
  } catch (error) {
    
    if(error.response.status ===404){

        document.getElementById("error").innerHTML = "❌ Error: User ID not found.";
        return false;
    }
    else {
        document.getElementById("error").innerHTML = `❌ Error: Something went wrong ${error.message}.`;
    }  
  }
  return true;

}

//Password reset 
async function passwordReset( id, newPassword) {

    try {
      
       const response = await axios.get(`https://api.restful-api.dev/objects/${id}`);
  
      const email = response.data.data.email; 
      const address= response.data.data.address;
      
      const updatedData = {
        data:{
        email,
        password:newPassword,
        address,
        }
      };
    
      await axios.patch(`https://api.restful-api.dev/objects/${id}`, updatedData );
              
      document.getElementById("error").innerHTML = "✅ Password updated successfully!";
    
  
    } catch (error) {
      console.error("Error:", error.message)
  
    }
    
  }

passResetButton.addEventListener("click", async () => {
    
    const userID = document.getElementById("userID-input").value;
    const currentPassword = document.getElementById("currentpass-input").value
    const newPassword = document.getElementById("newpass-input").value
    const confirmPassword = document.getElementById("confirmpass-input").value
    
   const isValid = await validateFields (userID, currentPassword,newPassword, confirmPassword );
    
  if (isValid){
    await passwordReset(userID, confirmPassword)
    
    const form = document.querySelector("form");
    if (form) {
        form.reset();
    }
  }
    

});


 