async function getUser(id) {

  try {
    
    const response = await axios.get(`https://api.restful-api.dev/objects/${id}`);
  
    console.log("User found:");
    console.log("User data:", response.data);
   return response.data;
      
  } catch (error) {
    if(error.response.status === 404){
       console.error("Error: User not found.")
       return { error: "User not found" };
    }
    else{  console.error(`Error: ${error.message}`);}
    return { error: `Error: ${error.response.status}` };
   
    
  }
  
}

getUser("ff808181932badb6019515861b4c47")


