async function getUserById(){

  const response = await fetch(`https://reqres.in/api/users/2`);
  const data =  await response.json();
  console.log("Datos del usuario:", data.data)
  

}

getUserById();