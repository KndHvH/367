from flask import Flask, render_template, redirect, request, session, flash


class User:
    def __init__(self, name, email, password) -> None:
        self.__name = name
        self.__email = email
        self.__password = password

    @property
    def name(self):
        return self.__name.title()

    @property
    def email(self):
        return self.__email

    @property
    def password(self):
        return self.__password


class UserList:
    def __init__(self, users) -> None:
        self.__users = users

    def __getitem__(self, item):
        return self.__users[item]

    def __len__(self):
        return len(self.__users)

    @property
    def users(self):
        return self.__users


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


game1 = Game('Tetris', 'Puzzle', 'Atari')
game2 = Game('Csgo', 'Fps', 'PC')
game3 = Game('Skyrim', 'Rpg', 'Ps3')

gamesList = [game1, game2, game3]


matias = User('matias', 'delend89@gmail.com', '1234')
user2 = User('joao', '12345@gmail.com', '12345')

users = UserList([matias, user2])

logged = False

app = Flask(__name__)
app.secret_key = '09450425'


@app.route('/')
def index():
    return redirect('http://127.0.0.1:8080/home')


@app.route('/home')
def home():
    return render_template('list.html', title='Games', games=gamesList)


@app.route('/addgame')
def addgame():
    if 'username' in session:
        if session['username'] != None:
            return render_template('add.html', title='New Game')
    return redirect('http://127.0.0.1:8080/login?n=addgame')


@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']

    game = Game(name, category, console)
    gamesList.append(game)

    return redirect('http://127.0.0.1:8080/home')


@app.route('/login')
def login():
    return render_template('login.html', title='Login')


@app.route('/logincheck', methods=['POST'])
def logincheck():
    email = request.form['email']
    password = request.form['password']

    for user in users:
        if email == user.email and password == user.password:
            session['username'] = user.name
            flash(session['username'] + ' logged!')
            return redirect('http://127.0.0.1:8080/addgame')
        flash('not logged!')
        return redirect('http://127.0.0.1:8080/login')
    
@app.route('/logout')
def logout():
    session['username'] = None
    flash('logged out')
    return redirect('htps://127.0.0.1:8080/home')


app.run(host='0.0.0.0', port=8080, debug=True)
