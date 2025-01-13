// Entrada
const student = {
	name: "John Doe",
	grades: [
		{name: "math",grade: 80},
		{name: "science",grade: 100},
		{name: "history",grade: 60},
		{name: "PE",grade: 90},
		{name: "music",grade: 98}
	]
}

// Proceso
const newArray = student.grades.map(item => item.grade);
let sum = newArray.reduce((a,b) => a+b) / newArray.length;

let nameMax = student.grades.findIndex (item => item.grade === Math.max(...newArray));
nameMax = student.grades[nameMax].name;

let nameMin = student.grades.findIndex (item => item.grade === Math.min(...newArray));
nameMin = student.grades[nameMin].name;

//Salida
const result ={
    name:student.name,
    gradeAvg: sum,
	highesGrade: nameMax,
	lowestGrade: nameMin
}

console.log(result);