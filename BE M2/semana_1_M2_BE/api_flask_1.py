import json
from flask import Flask, jsonify, request

app = Flask(__name__)

def read_tasks():
    with open("tasks.json", "r") as file:
        return json.load(file)
    
def write_tasks(tasks):
    with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)


def validate_task(task):

    # Validate required fields
    if "title" not in task:
        return jsonify({"error": "The 'title' field is required"}), 400

    if "description" not in task:
        return jsonify({"error": "The 'description' field is required"}), 400

    if "status" not in task:
        return jsonify({"error": "The 'status' field is required"}), 400

    # Validate that the status is one of the allowed ones.
    if task["status"] not in ["To Do", "In Progress", "Completed"]:
        return jsonify({"error": "The 'status' field should be 'To Do', 'In Progress' or 'Completed'."}), 400
    
    return None


@app.route("/tasks", methods=["GET"])
def get_tasks():
    status = request.args.get("status")
    tasks = read_tasks()

    if status:
        tasks = [task for task in tasks if task["status"] == status]

    return jsonify(tasks)


@app.route("/tasks", methods=["POST"])
def create_tasks():
    try:
        # Get the task from the application
        task = request.get_json()

        # Validar campos obligatorios
        if "id" not in task:
            return jsonify({"error": "The 'id' field is required."}), 400

        if task["id"] in [t["id"] for t in read_tasks()]:
            return jsonify({"error": "The task ID already exists."}), 400

        # Validate the rest of the fields
        error = validate_task(task)
        if error:
            return error

        # Save the new task
        tasks = read_tasks()
        tasks.append(task)
        write_tasks(tasks)

        return jsonify(task), 201

    except ValueError as ex:
        return jsonify({"message": str(ex)}), 400

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
	

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    
     #Update a task by its ID.
	# The task ID is passed as a URL parameter.
    tasks = read_tasks()
    task_id = int(task_id)
    
    task_data = request.get_json()
	# Validate required fields
    error = validate_task(task_data)
    if error:
        return error

    # Search and update the corresponding task
    for task in tasks:
        if task["id"] == task_id:
            task.update(task_data)
            write_tasks(tasks)    

            return jsonify(task), 200
            
        
    return jsonify({"error": "Task not found"}), 404

    
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
  
    # Deletes a task by its ID.
    tasks = read_tasks()
    # Filter the list to exclude the task with the specified ID
    tasks = [task for task in tasks if task["id"] != int(task_id)]
    write_tasks(tasks)

    return jsonify(tasks)
	

if __name__ == "__main__":
    app.run(host="localhost", debug=True)
    
