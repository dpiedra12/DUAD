const fs = require('fs');

function main() {
  let firstArray = [];
  let secondArray = [];

  const logData = (targetArray) => (err, data) => {
   
    let myArray = data.split("\n").map(word => word.trim()).filter(word => word);
    targetArray.push(...myArray);
    

    if (firstArray.length && secondArray.length) {
      compareWords();
    }
  };

  function compareWords() {
    let commonWords = firstArray.filter((word) => secondArray.includes(word));
    console.log( `The hidden message is: ${commonWords.join(" ")}`);
  }

  fs.readFile('SEMANA 7/file1.txt', 'utf8', logData(firstArray));
  fs.readFile('SEMANA 7/file2.txt', 'utf8', logData(secondArray));


}

main();
