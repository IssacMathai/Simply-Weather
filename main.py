from flask import Flask, request, make_response, jsonify

app = Flask('simply-weather')

@app.route('/')
def no_data():
    response = jsonify({'message': 'Hello there!', 'info': 'Using jsonify...', 'status': 200})
    return response

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

app.run()