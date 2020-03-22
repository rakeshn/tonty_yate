# Twenty Eight - the ultimate card game

This repo contains the api gateway for the card game
Functions include:

* Starting a game
* Joining a game as a player
* Shuffling the deck and
* dealing the cards to players


## APIs

* GET /games        - Gets all the game ids that are active
* PUT /game         - Create a new game
* POST /game/start  - Start the game
* PUT /game/gameid/player - Register a new player