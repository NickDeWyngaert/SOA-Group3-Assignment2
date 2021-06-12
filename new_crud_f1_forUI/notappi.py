from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

basedir = os.path.abspath(os.path.dirname(__file__))

notappi = Flask(__name__)
notappi.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
notappi.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Order matters: Initialize SQLAlchemy before Marshmallow
db = SQLAlchemy(notappi)
ma = Marshmallow(notappi)

class f1_team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    naam = db.Column(db.String(255))
    budget = db.Column(db.String(255))
    beschrijving = db.Column(db.String(255))

    def __init__(self, naam, budget, beschrijving):
        self.naam = naam
        self.budget = budget
        self.beschrijving = beschrijving

class F1_teamsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'naam', 'budget', 'beschrijving')


f1_team_schema = F1_teamsSchema()
f1_teams_schema = F1_teamsSchema(many=True)


@notappi.route('/f1_teams', methods=['GET'])
def get_f1_teams():
    all_f1_teams = f1_team.query.all()
    result = f1_teams_schema.dump(all_f1_teams)

    return jsonify(result)



@notappi.route('/f1_teams', methods=['POST'])
def add_f1_team():
    naam = request.json['naam']
    budget = request.json['budget']
    beschrijving = request.json['beschrijving']

    new_f1_team = f1_team(naam, budget, beschrijving)

    db.session.add(new_f1_team)
    db.session.commit()

    return f1_team_schema.jsonify(new_f1_team)

@notappi.route('/f1_teams/<id>', methods=['GET'])
def get_f1_team(id):
    f1_teamx = f1_team.query.get(id)
    return f1_team_schema.jsonify(f1_teamx)

@notappi.route('/f1_teams/<id>', methods=['DELETE'])
def delete_f1_teams(id):
    f1_teamx = f1_team.query.get(id)
    db.session.delete(f1_teamx)
    db.session.commit()

    return f1_team_schema.jsonify(f1_teamx)

@notappi.route('/f1_teams/<id>', methods=['PUT'])
def update_f1_teams(id):
    f1_teamx = f1_team.query.get(id)
    naam = request.json['naam']
    budget = request.json['budget']
    beschrijving = request.json['beschrijving']

    f1_teamx.naam = naam
    f1_teamx.budget = budget
    f1_teamx.beschrijving = beschrijving

    db.session.commit()

    return f1_team_schema.jsonify(f1_teamx)


if __name__ == '__main__':
    notappi.run(host='127.0.0.1', port=5000,debug=True)