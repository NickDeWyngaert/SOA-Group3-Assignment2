from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)

# Init ma
ma = Marshmallow(app)

# ToDoItem class
class ToDoItem(db.Model):
    """docstring for ToDoItem."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    course = db.Column(db.String(100))
    task = db.Column(db.String(100))

    def __init__(self, name, course, task):
        self.name = name
        self.course = course
        self.task = task

# ToDoItem Schema
class ToDoItemSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'course', 'task')

# Init schema
todoitem_schema = ToDoItemSchema()
todoitems_schema = ToDoItemSchema(many=True)

# Create ToDoItem
@app.route('/todoitems', methods=['POST'])
def add_todoitem():
    name = request.json['name']
    course = request.json['course']
    task = request.json['task']

    new_todoitem = ToDoItem(name, course, task)

    db.session.add(new_todoitem)
    db.session.commit()

    return todoitem_schema.jsonify(new_todoitem)

# Get all todoitems
@app.route('/todoitems', methods=['GET'])
def get_todoitems():
    all_todoitems = ToDoItem.query.all()
    result = todoitems_schema.dump(all_todoitems)

    return jsonify(result)

# Get single todoitem
@app.route('/todoitems/<id>', methods=['GET'])
def get_todoitem(id):
    todoitem = ToDoItem.query.get(id)
    return todoitem_schema.jsonify(todoitem)

# Update a todoitem
@app.route('/todoitems/<id>', methods=['PUT'])
def update_todoitem(id):
    todoitem = ToDoItem.query.get(id)

    name = request.json['name']
    course = request.json['course']
    task = request.json['task']

    todoitem.name = name
    todoitem.course = course
    todoitem.task = task

    db.session.commit()

    return todoitem_schema.jsonify(todoitem)

# Delete todoitem
@app.route('/todoitems/<id>', methods=['DELETE'])
def delete_todoitem(id):
    todoitem = ToDoItem.query.get(id)
    db.session.delete(todoitem)
    db.session.commit()

    return todoitem_schema.jsonify(todoitem)

# Run Server
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000,debug=True)
