from flask import Flask, request, make_response, jsonify, render_template
import requests
import os

app = Flask(__name__)

WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

dict_with_weather_info = {
    'Taupo': [20, 'Sunny'],
    'Wellington': [12, 'Cloudy'],
    'Christchurch': [9, 'Rainy']
}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city_name = request.form.get('city_name')
        update_specific_city_weather(city_name)

    return render_template('index.html', weather=dict_with_weather_info)


def update_specific_city_weather(city_name):
    # Get lat and lon
    payload = {'q': city_name, 'appid': WEATHER_API_KEY}
    r = requests.get('http://api.openweathermap.org/geo/1.0/direct', params=payload)
    lat = r.json()[0]['lat']
    lon = r.json()[0]['lat']

    # Get weather
    payload = {'lat': lat, 'lon': lon, 'units': 'metric', 'appid': WEATHER_API_KEY}
    r = requests.get('https://api.openweathermap.org/data/2.5/weather', params=payload)
    state = r.json()['weather'][0]['main']
    temp = r.json()['main']['temp']
    dict_with_weather_info[city_name] = [state, round(temp)]


def update_all_weather():
    for city, info in dict_with_weather_info.items():
        update_specific_city_weather(city)


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
    update_all_weather()
    app.run(debug=True)
