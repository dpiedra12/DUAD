const pokemon= fetch (`https://reqres.in/api/users/23`);
pokemon.then ((response)=>{
    if(!response.ok){

        throw new Error (`El usuario no se encontró.`);
    }
    return response.json();
    
}).then((data)=>{
    console.log(data.data); 

}).catch((error)=>{
    console.log(`${error}`);
  }).finally(()=>{
    console.log("La solicitud se ha completado");
});
  


