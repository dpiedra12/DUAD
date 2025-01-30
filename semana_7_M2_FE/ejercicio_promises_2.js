function getPokemon(pokemonID){

    return fetch (`https://pokeapi.co/api/v2/pokemon/${pokemonID}`)
    .then((response) => response.json()) 
    .then((data) => data.name);
          

  }
  
  Promise.any([getPokemon(22), getPokemon(323), getPokemon(12)])
.then (name => console.log(`El primer pokemón obtenido es:`, name) )