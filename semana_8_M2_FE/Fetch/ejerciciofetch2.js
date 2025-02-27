async function createUser(name, email, password, address){

  try {
    const response = await fetch("https://api.restful-api.dev/objects",{
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        name: name,
        data: {
          email: email,
          password: password,
          address: address
        }
      })
    });
    if(!response.ok){
      throw new Error (`Error en la solicitud: ${response.statusText}`)
    }
      const newData = await response.json()
      console.log(`Registro creado`, newData);
  
    
  } catch (error) {
    console.error("Error:", error.message)
  }
}

createUser("Danny", "danny@gmail.com", "1234", "San Jose")