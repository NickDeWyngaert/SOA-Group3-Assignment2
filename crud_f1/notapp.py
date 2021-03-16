from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

class f1_team:
    def __init__(self, naam, budget, beschrijving):
        self.naam = naam
        self.budget = budget
        self.beschrijving = beschrijving

f1_teams = [
    {
        'naam' : 'Red Bull',
        'budget' : 140000000,
        'beschrijving' : 'dit is een beschrijving'
    }
]

@app.route('/f1_teams', methods=['GET'])
def get_f1_teams():
    return jsonify({'f1_teams': f1_teams})

@app.route('/f1_teams/create', methods=['POST'])
def add_f1_team():
    f1_team = request.get_json(force=True)
    f1_teams.append(f1_team)
    return jsonify({'f1_teams': f1_teams})

@app.route('/f1_teams/delete/<int:index>', methods=['DELETE'])
def delete_f1_team(index):
    f1_teams.pop(index)
    return 'None', 200

@app.route('/f1_teams/update/<int:index>', methods=['PUT'])
def update_f1_team(index):
    f1_team = request.get_json(force=True)
    f1_teams[index] = f1_team
    return jsonify(f1_teams[index]), 200

if __name__ == '__main__':
    app.run(debug=True)
