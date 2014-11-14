from flask import Flask
from flask import request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

# @app.route('/hello')
# def hello():
#     return 'Hello World'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

def valid_login(username, password):
    pass

def log_the_user_in(username):
    pass


@app.route('/login', methods=['POST', 'GET'])
def login():
    searchword = request.args.get('key', '')
    error = None
    print searchword
    if request.method == 'POST':
        print request.form['username']
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

@app.route('/jsonExample')
def jsonExample():
    exampleDic = {'a' : [1,2,3], 'b' : [5,6,7]}
    a=json.dumps(exampleDic)
    return str(a)
    
@app.route('/topla', methods=['POST', 'GET'])
def toplaExample():
    if request.method == 'POST':
        app.logger.debug('Entered POST')
        f1 = int(request.form['FirstNumber'])
        app.logger.debug('F1', f1)
        f2 = int(request.form['LastNumber'])
        app.logger.debug('F2', f2)
        return render_template('result.html', result=f1+f2)
    return render_template('topla.html')
    # the code below is executed if the request method
    # was GET or the credentials were invalid
        


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)