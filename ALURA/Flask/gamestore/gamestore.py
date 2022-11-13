from flask import Flask, render_template, redirect, request


class Game:
    def __init__(self, name, category, console) -> None:
        self.__name = name
        self.__category = category
        self.__console = console

    @property
    def name(self):
        return self.__name

    @property
    def category(self):
        return self.__category

    @property
    def console(self):
        return self.__console


game1 = Game('Tetis', 'Puzzle', 'Atari')
game2 = Game('Csgo', 'Fps', 'PC')
game3 = Game('Skyrim', 'Rpg', 'Ps3')

gamesList = [game1, game2, game3]

app = Flask(__name__)


@app.route('/')
def index():
    return redirect('http://127.0.0.1:8080/home')


@app.route('/home')
def home():

    return render_template('list.html', columnTitle='Jogos', games=gamesList)


@app.route('/addgame')
def addgame():
    return render_template('add.html', title='New Game')


@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']

    game = Game(name, category, console)
    gamesList.append(game)

    return redirect('http://127.0.0.1:8080/home') 


app.run(host='0.0.0.0', port=8080, debug=True)
