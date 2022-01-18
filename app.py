from logging import debug
from tkinter import N
from flask import Flask, render_template, redirect, request
from flask import json as fjson
from Minesweeper import Gamefield
from flask_socketio import SocketIO,emit
#! don't create game with starting the server

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = b'\x0f\xf6j\x07E\xb9an\x9d4\x19\xa0'
socketio = SocketIO(app) # replaces the app.run() command #use logger=True, engineio_logger=True for debugging



@socketio.on('connect')
@app.route("/", methods=['GET', 'POST'])
def index():# define data to give from back-end to front-end\
    global newGame
    newGame = Gamefield()
    # create Gamefield object
    
    message = newGame.toJSON()
    socketio.emit('initialize',message)
    return render_template('Gamefield.html')


#TODO: Send initialized gamefield through via websocket
# Deploy JSON object in Flask for external uses in JS file
# @app.route("/startGame", methods=['GET', 'POST']) # access this with fetch api in js
# def testGame(): 
#     # GET request is default method 
#     message = newGame.toJSON() # return is string
    
#     #writter(message)
#     return message

    
@socketio.on('click')
def handle_message(json):
    tile = json['tile']
    newGame.isLightUpChanger(tile['x'],tile['y'])
    message = newGame.toJSON()
    emit('newjson',message)
    
    #writter(message)

#json data for using in jupyternotebook test
def writter(data):
    f = open("dump.txt",'a')
    f.write(str(data))
    f.close

if __name__ == '__main__':
    socketio.run(app)



