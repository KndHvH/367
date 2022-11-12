from flask import Flask, render_template

app = Flask(__name__)


@app.route('/main')
def main():
    return render_template('list.html',columnTitle = 'Jogos')


app.run(host='0.0.0.0', port=8080)
