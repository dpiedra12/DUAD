async function getUserData() {
    console.log("Requesting data...");
    const response = await fetch(`https://api.restful-api.dev/objects`);
    console.log("Data retrieved!");
    return response.json();
}

async function main() {

	try {
			
	const nullData = await getUserData();
	let data = nullData.filter(element => element.data !== null);
	
	data.forEach(element => {
	  
	 const newData = Object.entries(element.data).map(([key, value]) => `${key}: ${value}`).join(", ")
	  console.log(`${element.name} (${newData})`)
	  
	});
		
	} catch (error) {
		console.error("Error fetching data:", error);
	}
}

main()


