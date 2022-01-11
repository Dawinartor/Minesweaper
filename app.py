from logging import debug
from flask import Flask, render_template, redirect, request
from Minesweeper import Gamefield
from flask_socketio import SocketIO
#! don't create game with starting the server


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = b'\x0f\xf6j\x07E\xb9an\x9d4\x19\xa0'
socketio = SocketIO(app)

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
    socketio.run(app)
    #app.run(debug=True)
