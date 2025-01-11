const example = "This is a string in javascript!";
let result = [];
let newWord = "";

for (let i = 0; i < example.length; i++) {
  if (example[i] !== " ") {
    newWord += example[i];
  } else {
    result.push(newWord);
    newWord = "";
  }
  if (i === example.length - 1) {
    result.push(newWord);
  }
}

console.log(result);

