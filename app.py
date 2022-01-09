from flask import Flask, render_template, redirect, request
from Minesweeper import Gamefield

# create Gamefield object
newGame = Gamefield()

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('Gamefield.html')
        


if __name__ == '__main__':
    app.run(debug=True)