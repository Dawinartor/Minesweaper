from flask import Flask, render_template, redirect, request, jsonify
from Minesweeper import Gamefield
#! don't create game with starting the server


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():                                # define data to give from back-end to front-end
        # create Gamefield object
    return render_template('Gamefield.html')


# test Flask JSON object using in external JS file
@app.route("/startGame", methods=['GET', 'POST']) # access this with fetch api in js
def testGame(): 
    # GET request is default method
    newGame = Gamefield()
    message = newGame.toJSON() # return is string
    return message
        


if __name__ == '__main__':
    app.run(debug=True)