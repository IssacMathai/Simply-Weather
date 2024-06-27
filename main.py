from flask import Flask

app = Flask('simply-weather')

@app.route('/')  
def render_main():  
    return 'This is the main page'

@app.route('/all')
@app.route('/about')  
def render_about():  
    return 'Project Information'

@app.route('/user/<username>/')
def show_profile(username):
    return "Username: " + username


app.run()