#!/usr/bin/env python3
# Test in Python 3.7.3

'''
This Flask application is deployed on Gunicorn.
The command line arguments are:
> gunicorn --bind 0.0.0.0:5000 --workers 8 --access-logfile - --error-logfile - server:app
'''
from flask import Flask, request, redirect, render_template
import traceback, uuid, os, shutil

'''
This function is used to check if a Pokémon exists or not.
We will connect to remote Pokemon Wiki to check this.

Note the domain 'pokemon.fandom.com' has nothing to do with this challenge.
DO NOT ATTACK THIS DOMAIN.
'''
from requests import session
http_client = session()
def doesPokemonExist(name):
    if http_client.get('https://pokemon.fandom.com/wiki/' + name).status_code == 404:
        # 404 Not found
        return False
    return True

'''
template_folder is '.', which means the current directory will be used.
`index.html` will be used for rednering HTML template.
'''
app = Flask(__name__, template_folder='.')

DB_DIR = '/tmp/'
INIT_COIN = 500
INIT_POKEMON = 'Magikarp'
POKEMON_PRICES = {
    'Magikarp': 1,
    'Slowpoke': 217,
    'Eevee': 388,
    'Snorlax': 499,
}

class Database():
    def createNewUser():
        user_id = str(uuid.uuid4())
        os.mkdir(f'{DB_DIR}/{user_id}')
        __class__.saveCoinBy(user_id, INIT_COIN)
        __class__.addPokemonBy(user_id, INIT_POKEMON)
        return user_id

    def deleteUser(user_id):
        shutil.rmtree(f'{DB_DIR}/{user_id}')

    def saveCoinBy(user_id, coin):
        with open(f'{DB_DIR}/{user_id}/coin', 'w') as f:
            print(coin, file=f)

    def addPokemonBy(user_id, pokemon):
        '''
        We will append a new line for the new pokemon.
        '''
        with open(f'{DB_DIR}/{user_id}/pokemons', 'a') as f:
            print(pokemon, file=f)

    def getCoinPokemonsBy(user_id):
        with open(f'{DB_DIR}/{user_id}/coin') as f:
            coin = int(f.read())
        with open(f'{DB_DIR}/{user_id}/pokemons') as f:
            pokemons = f.read().strip().splitlines()
        return coin, pokemons


@app.route('/')
def register():
    user_id = Database.createNewUser()
    return redirect(f'/{user_id}/')

'''
Note if the URL does not follow the UUID4 format,
Flask will not invoke this `index` function.
'''
@app.route('/<uuid:user_id>/')
def index(user_id):
    coin, pokemons = Database.getCoinPokemonsBy(user_id)
    unique_user_pokemons = set(pokemons)
    all_pokemons = set(POKEMON_PRICES.keys())
    if unique_user_pokemons == all_pokemons:
        with open('./flag.txt') as f:
            msg = 'Well-done! Here is your flag: ' + f.read().strip()
        Database.deleteUser(user_id)
    else:
        msg = 'Are you a Pokémon master? Catch all Pokémons to get the flag!'
    return render_template('index.html', coin=coin, pokemons=pokemons, POKEMON_PRICES=POKEMON_PRICES, msg=msg)

@app.route("/<uuid:user_id>/buy")
def buy(user_id):
    '''
    Extract the pokemon name from the GET parameter `http://example.com/?name=pokemon_name`
    '''
    name = request.args['name']
    coin, pokemons = Database.getCoinPokemonsBy(user_id)
    if coin < POKEMON_PRICES[name]:
        return "You don't have enough PokémonCoin to buy this Pokémon!"
    if not doesPokemonExist(name):
        return "Hey! It's not a Pokémon! Are you sure it's not a Digimon?"

    coin -= POKEMON_PRICES[name]
    Database.saveCoinBy(user_id, coin)
    Database.addPokemonBy(user_id, name)
    pokemons.append(name)
    msg = f'You bought {name}!'
    return render_template('index.html', coin=coin, pokemons=pokemons, POKEMON_PRICES=POKEMON_PRICES, msg=msg)

@app.errorhandler(Exception)
def all_exception_handler(exception):
   return '<pre>' + traceback.format_exc() + '</pre>'
