from flask import Flask, render_template, redirect, request
from Minesweeper import Gamefield

# create Gamefield object
newGame = Gamefield()

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():                                # define data to give from back-end to front-end
    return render_template('Gamefield.html')


# test Flask JSON object using in external JS file
@app.route("/newGame", methods=['GET', 'POST'])
def testGame():
    data = newGame.toJSON()
    return render_template('Gamefield.html',data=data)
        


if __name__ == '__main__':
    app.run(debug=True)