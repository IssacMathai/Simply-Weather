from flask import Flask

app = Flask('simply-weather')

@app.route('/')
def index():
   return 'Hello World!'


app.run()