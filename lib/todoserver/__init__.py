# todoserver/__init__.py

from flask import Flask, make_response, request
import json
app = Flask(__name__)

MEMORY = {}

@app.route("/tasks/", methods=["GET"])
def get_all_tasks():
    tasks = [{"id": task_id, "summary": task["summary"]}
            for task_id, task in MEMORY.items()]
    return make_response(json.dumps(tasks), 200)

@app.route("/tasks/", methods=["POST"])
def create_task():
    #request.data.decode("utf-8")
    payload = request.get_json(force=True)
    try: 
        task_id = 1 + max(MEMORY.keys())
    except ValueError:
        task_id = 1
    MEMORY[task_id] = {
        "summary": payload["summary"],
        "description": payload["description"],
    }
    task_info = {"id": task_id}
    return make_response(json.dumps(task_info), 201)

@app.route("/tasks/<int:task_id>/", methods=["GET"])
def task_details(task_id):
    task_info = MEMORY[task_id].copy()
    task_info["id"] = task_id 
    return json.dumps(task_info)

if __name__ == "__main__":
    app.run()



