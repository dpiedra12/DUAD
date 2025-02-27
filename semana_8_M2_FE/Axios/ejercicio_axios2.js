async function createUser(name, email, password, address){

  const data={
    name: name,
    data: {
      email: email,
      password: password,
      address: address
    }
  }
  try {
  
    const response = await axios.post("https://api.restful-api.dev/objects", data);
    console.log(`Registro creado`, response.data);
    
  
  } catch (error) {
    console.error("Error:", error.message);


  }
}

createUser("Danny", "danny@gmail.com", "*****", "Belen")