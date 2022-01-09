from flask import Flask, render_template, redirect, request
from Minesweeper import Gamefield

# create Gamefield object
newGame = Gamefield()

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():                                # define data to give from back-end to front-end
    return render_template('Gamefield.html')


# test Flask requesting data

@app.route('/query-example')
def query_example():
    user = {'firstname': "Mr.", 'lastname': "My Father's Son"}
    return render_template('Gamefield.html', data = user)

@app.route('/form-example')
def form_example():
    return 'Form Data Example'

@app.route('/json-example', methods=['GET'])
def json_example():
    request.json = request.get_json()
    testJsonObject = newGame.toJSON()
    language = request.args.get('language')
    return '''<h1>The language value is: {}</h1>'''.format(testJsonObject)

        


if __name__ == '__main__':
    app.run(debug=True)