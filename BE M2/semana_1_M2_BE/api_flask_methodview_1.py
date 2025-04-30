import json
from flask import Flask, jsonify, request
from flask.views import MethodView

app = Flask(__name__)

class TaskAPI(MethodView):
    def read_tasks(self):
        with open("tasks.json", "r") as file:
            return json.load(file)

    def write_tasks(self, tasks):
        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)

    def validate_task(self, task):
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
        

    def get(self):
        status = request.args.get("status")
        tasks = self.read_tasks()

        if status:
            tasks = [task for task in tasks if task["status"] == status]

        return jsonify(tasks)

    def post(self):
        try:
            # Get the task from the application
            task = request.get_json()

            # Validar campos obligatorios
            if "id" not in task:
                return jsonify({"error": "The 'id' field is required."}), 400

            if task["id"] in [t["id"] for t in self.read_tasks()]:
                return jsonify({"error": "The task ID already exists."}), 400

            # Validate the rest of the fields
            error = self.validate_task(task)
            if error:
                return error

            # Save the new task
            tasks = self.read_tasks()
            tasks.append(task)
            self.write_tasks(tasks)

            return jsonify(task), 201

        except ValueError as ex:
            return jsonify({"message": str(ex)}), 400

        except Exception as ex:
            return jsonify({"message": str(ex)}), 500


    def put(self, task_id):
        # Update a task by its ID.
        # The task ID is passed as a URL parameter.
        tasks = self.read_tasks()
        task_id = int(task_id)

        task_data = request.get_json()
        # Validate required fields
        error = self.validate_task(task_data)
        if error:
            return error

        # Search and update the corresponding task
        for task in tasks:
            if task["id"] == task_id:
                task.update(task_data)
                self.write_tasks(tasks)    

                return jsonify(task), 200
        
        return jsonify({"error": "Task not found"}), 404


    def delete(self, task_id):
        # Deletes a task by its ID.
        tasks = self.read_tasks()
        # Filter the list to exclude the task with the specified ID
        tasks = [task for task in tasks if task["id"] != int(task_id)]
        self.write_tasks(tasks)

        return jsonify(tasks)


task_view = TaskAPI.as_view('task_api')
app.add_url_rule('/tasks', view_func=task_view, methods=['GET',])
app.add_url_rule('/tasks', view_func=task_view, methods=['POST',])
app.add_url_rule('/tasks/<int:task_id>', view_func=task_view, methods=[ 'PUT', 'DELETE'])


if __name__ == "__main__":
    app.run(debug=True, port=5000)
