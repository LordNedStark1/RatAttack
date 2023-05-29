from flask import Flask, request

from AppUtils.word_generator.WordGenerator import WordGenerator
from services.PlayerService.PlayerServiceImpl import PlayerServiceImpl
from services.PlayerService.PlayerServiceInterface import PlayerServiceInterface
from services.game_service.GameServiceImpl import GameServiceImpl
from services.game_service.GameServiceInterface import GameServiceInterface

app = Flask(__name__)
player_service: PlayerServiceInterface = PlayerServiceImpl()
house_service: GameServiceInterface = GameServiceImpl()


@app.route('/', methods=['POST'])
def create_new_game():
    data = request.get_json()
    player_name = data.get('player_name')
    player_age = data.get('player_age')

    if player_name is None:
        player_name = WordGenerator.generate_name()

    game_id , player_id =player_service.create_new_player(player_name, player_age)

    return "Welcome to RatAttack " + str(player_name) + \
           "\n player id is = " + str(player_id) + \
           "\n game id is = " + game_id

@app.route('/', methods=['GET'])
def find_game_by_id():
    data = request.get_json()
    game_id = data.get('game_id')
    return house_service.find_game_by_id(game_id)



def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
