async function getUserById(){

  try {
  const response = await fetch(`https://reqres.in/api/users/23`);
  if (!response.ok){

    throw new Error ('El usuario no se encontró.')
  }
  const data =  await response.json();
  console.log('Datos del usuario:', data.data)
  }
  catch(error){
    console.log(`Error:  ${error.message}`);

  }
  

}

getUserById();