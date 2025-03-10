async function updateUser( id, newAddress) {

  try {
    
    const getResponse = await fetch(`https://api.restful-api.dev/objects/${id}`);
   
    if(!getResponse.ok){
      throw new Error ('El usuario no se encontró.')

    }
    const currentData =  await getResponse.json();


    const updateData ={
      data:{
        ...currentData.data,
        address:newAddress
      }
    }
        
    const patchResponse = await fetch(`https://api.restful-api.dev/objects/${id}`,{
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(updateData)
  
    });

    if(!getResponse.ok){
      throw new Error ('El usuario no se actualizó.')

    }

    const updatedUser = await patchResponse.json();
    console.log(`Registro actualizado`, updateData);
    return updatedUser;
    
  } catch (error) {
    console.error("Error:", error.message)
  }
}

updateUser("ff808181932badb6019514c237b0466f", "Heredia")