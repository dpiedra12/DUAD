async function updateUser( id, newAddress) {

  try {
    
     const response = await axios.get(`https://api.restful-api.dev/objects/${id}`);

    const email = response.data.data.email; 
    const password = response.data.data.password;
    
    const updatedData = {
      data:{
      email,
      password,
      address: newAddress
      }
    };
  
    const patchResponse = await axios.patch(`https://api.restful-api.dev/objects/${id}`, updatedData );
      
    console.log("El usuario se ha actualizado", patchResponse.data)


  } catch (error) {
    console.error("Error:", error.message)

  }
}

updateUser("ff808181932badb601951a08485c54cb", "Manuel")