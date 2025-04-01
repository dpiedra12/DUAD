window.onload = () => {
  
  const userData = localStorage.getItem("data");
  if (!userData) {
    document.body.innerHTML = "<h1>Redirecting to Sign in...</h1>";
    setTimeout(() => {
      location.href = "./login.html";
    }, 300); 
  }
};




const signButton = document.getElementById("sign-out");
const addTaskBtn = document.getElementById("add-btn");

async function addTask() {
  try {
    const userData = JSON.parse(localStorage.getItem('data'));
    const userID = userData.id;
    const email = userData.data.email;
    const password = userData.data.password;
    const address = userData.data.address;

    let tasks = userData.data.tasks;
    tasks ??= [];

    let newTaskText = document.getElementById("new-task-input").value;
    if (!newTaskText) {
      alert("Please insert a task.");
      return;
    }

    const newTask = {
      id: Date.now(),
      title: newTaskText,
      completed: false,
    };

    tasks.push(newTask);

    const data = {
      id: userID,
      data: {
        email: email,
        password: password,
        address: address,
        tasks: tasks,
      }
    };

    const response = await axios.patch(`https://api.restful-api.dev/objects/${userID}`, data);
    alert("Task added");

    localStorage.setItem("data", JSON.stringify(response.data));
    document.getElementById("task-list").innerHTML = "";
    getInfo();
    document.getElementById("new-task-input").value = "";
    clearRadioButtons();


  } catch (error) {
    document.getElementById("error").innerHTML = `❌ An error occurred: ${error.message}. Please try again.`;
  }
}

const completeRadio = document.getElementById("completed");
const incompleteRadio = document.getElementById("incompleted");

const clearRadioButtons = () => {
  getInfo();
  document.getElementById("completed").checked = false;
  document.getElementById("incompleted").checked = false;

};


async function getInfo() {
  try {
    const userData = JSON.parse(localStorage.getItem('data'));
    const userID = userData.id;

    if (userID) {
      const response = await axios.get(`https://api.restful-api.dev/objects/${userID}`);
      const tasks = response.data?.data?.tasks ?? [];
      renderTasks(tasks);
    }

  } catch (error) {
    document.getElementById("error").innerHTML = `An error occurred: ${error.message}`;
  }
}

const renderTasks = (tasks) => {
  const taskList = document.getElementById("task-list");
  taskList.innerHTML = "";

  tasks.forEach(task => {
    let newTask = document.createElement("li");
    newTask.classList.add("task");

    // Envuelve el texto de la tarea en un span
    let taskText = document.createElement("span");
    taskText.textContent = task.title + " ";
    if (task.completed) {
      newTask.classList.add("completed");
      
    }

    // Create and append delete button
    let deleteBtn = document.createElement("button");
    deleteBtn.textContent = "Delete";
    deleteBtn.onclick = async function () {
      
      const confirmDelete = confirm("Are you sure you want to delete this task?");
      if (!confirmDelete) {
        return; // If the user cancels, the task is not deleted.
      }
    
      // Proceed with deletion if the user confirms
      newTask.remove();
      const updatedTasks = tasks.filter(t => t.id !== task.id);
    
      const userData = JSON.parse(localStorage.getItem('data'));
      const data = {
        id: userData.id,
        data: {
          email: userData.data.email,
          password: userData.data.password,
          address: userData.data.address,
          tasks: updatedTasks,
        }
      };
    
      try {
        const response = await axios.patch(`https://api.restful-api.dev/objects/${userData.id}`, data);
        localStorage.setItem("data", JSON.stringify(response.data));
      } catch (error) {
        
        document.getElementById("error").innerHTML = "Error updating tasks: " + error.message;
      }
    };

    // Create and append checkbox
    let checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.checked = task.completed;
    checkbox.onchange = async function () {
      if (checkbox.checked) {
        newTask.classList.add("completed");
        task.completed = true;
      } else {
        newTask.classList.remove("completed");
        task.completed = false;
      }

      const userData = JSON.parse(localStorage.getItem('data'));
      const data = {
        id: userData.id,
        data: {
          email: userData.data.email,
          password: userData.data.password,
          address: userData.data.address,
          tasks: tasks,
        }
      };

      const response = await axios.patch(`https://api.restful-api.dev/objects/${userData.id}`, data);
      localStorage.setItem("data", JSON.stringify(response.data));
    };

    newTask.appendChild(checkbox);
    newTask.appendChild(taskText); // Add the text of the task
    newTask.appendChild(deleteBtn);
    taskList.appendChild(newTask);
  });
};

const toggleFilterTask = () => {
  
  const userData = JSON.parse(localStorage.getItem('data'));
  const tasks = userData.data.tasks;
  const filteredTasks = tasks.filter(task => 
    (document.getElementById("incompleted").checked && !task.completed) || 
    (document.getElementById("completed").checked && task.completed)
  );
  renderTasks(filteredTasks);
};


document.addEventListener("DOMContentLoaded", getInfo);

signButton.addEventListener("click", () => {

  setTimeout(function() { 
    alert("You have successfully logged out."); 
    localStorage.clear();                         
    location.href = "./login.html"; 
  }, 700); 
});


completeRadio.addEventListener("click", toggleFilterTask);
incompleteRadio.addEventListener("click", toggleFilterTask);