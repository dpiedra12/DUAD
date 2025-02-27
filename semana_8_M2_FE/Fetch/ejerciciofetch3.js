async function getUser(id) {
  try {
    const response = await fetch(`https://api.restful-api.dev/objects/${id}`);

    if (response.status === 404) {
      throw new Error('El usuario no se encontró.');
    }

    if (!response.ok) {
      throw new Error(`Error en la solicitud: ${response.statusText}`);
    }

    const data = await response.json();
    console.log("Datos del usuario:", data);
    return data;

  } catch (error) {
    console.error(`Error: ${error.message}`);
    return { error: error.message }; 
  }
}

getUser("ff808181932badb6019514c237b046");