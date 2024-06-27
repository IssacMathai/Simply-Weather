from flask import Flask, request, make_response, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hi! This is the response from the Flask application'


@app.route('/profile')
def profile():
    return 'This is profile page'


@app.route('/login')
def log_in():
    return 'This is login page'


@app.route('/data/get_error/')
def return_error():
    response = make_response('<p>Oops... Sounds like an error!</p>', 400)
    return response

@app.route('/all')
@app.route('/about')  
def render_about():  
    return 'This is a weather web app.'

@app.route('/user/<username>/')
def show_profile(username):
    return "Username: " + username

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        template = """
        <form method='POST'>
        <input type='text' placeholder='Username...'>
        <input type='password' placeholder='Password...'>
        <input type='submit' value='Auth'>
        </form>
        """
        return template

    elif request.method == 'POST':
        return 'Wow! Great, you logged in!'

if __name__ == '__main__':
   app.run(debug=True)