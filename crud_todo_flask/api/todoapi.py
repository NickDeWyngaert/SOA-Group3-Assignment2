from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

class todo_item:
    def __init__(self, name, course, soort):
        self.name = name
        self.course = course
        self.soort = soort


todo_items = [
    {
        'name' : 'Api aanmaken',
        'course': 'SOA',
        'soort' : 'Code schrijven'
    }
]

@app.route('/todo_items', methods=['GET'])
def get_todo_items():
    return jsonify({'todo_items': todo_items})


@app.route('/todo_items/create', methods=['POST'])
def add_todo_item():
    todo_item = request.get_json(force=True)
    todo_items.append(todo_item)
    return jsonify({'todo_items': todo_items})

@app.route('/todo_items/delete/<int:index>', methods=['DELETE'])
def delete_todo_item(index):
    todo_items.pop(index)
    return 'None', 200

@app.route('/todo_items/update/<int:index>', methods=['PUT'])
def update_todo_item(index):
    todo_item = request.get_json(force=True)
    todo_items[index] = todo_item
    return jsonify(todo_items[index]), 200

app.run(host='127.0.0.1', port=8000, debug=True)
