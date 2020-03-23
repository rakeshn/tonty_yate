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


@app.route('/game', methods=['PUT'])
def create_game():
    newgame = game.Game()
    active_games.append(newgame)
    return newgame.id


@app.route('/game/<id>/player', methods=['PUT'])
def register_player(id):
    if 'name' in request.args:
        name = request.args['name']

    game = get_game_by_id(id)
    return jsonify(game.register_player(name))


@app.route('/game/<id>/players', methods=['GET'])
def players(id):
    game = get_game_by_id(id)
    return jsonify([{player.name: player.team.name} for player in game.players])


@app.route('/game/<id>/start', methods=['POST'])
def start(id):
    game = get_game_by_id(id)
    game.start_game()
    return f"Started game {id}"


@app.route('/game/<id>/deal', methods=['POST'])
def deal(id):
    game = get_game_by_id(id)
    game.round.deal()
    return f"Done!"


@app.route('/game/<id>/player/<playerid>/hand', methods=['GET'])
def get_hand(id:str, playerid:str):
    game = get_game_by_id(id)
    if not game.started:
        raise Exception("Game has not started")
    player = [player for player in game.round.players if player.id == playerid]
    if not player:
        raise Exception("Player not found")

    return jsonify([str(card) for card in player[0].cards])


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