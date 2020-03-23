from flask import Flask, request, jsonify
from models import game
import json

app = Flask(__name__)

active_games = []


@app.route('/')
def hello_world():
    """Print 'Hello, world!' as the response body."""
    return 'Hello, world!'


@app.route('/games', methods=['GET'])
def games():
    ids = [g.id for g in active_games]
    return json.dumps(ids)


@app.route('/game', methods=['POST'])
def create_game():
    newgame = game.Game()
    active_games.append(newgame)
    return newgame.id


@app.route('/game/<id>/player', methods=['POST'])
def register_player(id):
    if 'name' in request.args:
        name = request.args['name']

    game = get_game_by_id(id)
    return jsonify(game.register_player(name))


@app.route('/game/<id>/players', methods=['GET'])
def players(id):
    game = get_game_by_id(id)
    return jsonify([player.name for player in game.players])


def get_game_by_id(_id) -> game.Game:
    if _id is None:
        raise Exception("Error: No id field provided. Please specify a game id.")

    game = [g for g in active_games if g.id == _id]
    if len(game) == 0:
        raise Exception('game not found')

    return game[0]




@app.route('/game', methods=['DELETE'])
def delete_game():
    if 'id' in request.args:
        _id = request.args['id']
    else:
        return "Error: No id field provided. Please specify a game id."

    prev_count = len(active_games)
    new_games = [g for g in active_games if g.id != _id]

    active_games.clear()
    active_games.extend(new_games)

    return jsonify(prev_count != len(new_games))

app.run()