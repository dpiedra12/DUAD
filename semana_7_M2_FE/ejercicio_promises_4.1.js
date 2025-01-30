const pokemon= fetch (`https://reqres.in/api/users/2`);
pokemon.then ((response)=>{
    return response.json();
}).then((data)=>{
    console.log(data.data); 

}).finally(()=>{
    console.log("La solicitud se ha completado");
});
  


