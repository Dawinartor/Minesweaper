from flask import Flask

app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def page1():
    return '''
    <form method="post">
        <button name="foo" value="upvote">Upvote</button>
    </form>'''    
        


if __name__ == '__main__':
    app.run(debug=True)