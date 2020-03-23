# Twenty Eight - the ultimate card game

This repo contains the api gateway for the card game
Functions include:

* Starting a game
* Joining a game as a player
* Shuffling the deck and
* dealing the cards to players


## APIs

* GET /games            - Gets all the game ids that are active
* PUT /game             - Create a new game
* POST /game/start      - Start the game
* PUT /game/{id}/player - Register a new player
* POST /game/start      - Start the game
* POST /game/deal       - Deal second hand
* GET /game/{id}/player/{playerid}/hand - Show a hand

## Playing the game

```bash
# list all games
curl 'http://localhost:5000/games'

# Create a new game
curl -XPUT 'http://localhost:5000/game'

# Register a new player
curl -XPUT 'http://localhost:5000/game/<id>/player?name=player1'

# List all players and team they belong to
curl 'http://localhost:5000/game/<id>/players'

# Start the game. This deals the first round
curl -XPOST 'http://localhost:5000/game/<id>/start'

# Show the hand of a player
curl 'http://localhost:5000/game/<id>/player/<playerid>/hand'

# Deal the second hand
curl -XPOST 'http://localhost:5000/game/<id>/deal'

# Start another round
curl -XPOST 'http://localhost:5000/game/<id>/start'

# Delete a game
curl -XDELETE 'http://localhost:5000/game/<id>'

```

## Setting up source code

- Install python 3
- Install Pipenv

- Install dependencies

    ```bash
    pipenv install
    ```

- Start pipenv shell
    ```bash
    pipenv shell
    ```
    
- Start the server
    ```bash
    python ./src/app.py
    ```
    
- Use the curl commands above