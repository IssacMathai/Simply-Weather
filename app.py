from flask import Flask, request, make_response, jsonify, render_template

app = Flask(__name__)

dict_with_weather_info = {
    'Taupo': [20, 'Sunny'],
    'Wellington': [12, 'Cloudy'],
    'Christchurch': [9, 'Rainy']
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city_name = request.form.get('city_name')
        dict_with_weather_info[city_name] = ['Unknown', 'Unknown']

    return render_template('index.html', weather=dict_with_weather_info)


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