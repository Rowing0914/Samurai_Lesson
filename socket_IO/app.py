from datetime import datetime
from flask import render_template
from FlaskWebProject2 import app
from flask_sockets import Sockets

@app.route('/')
def hello():
    return render_template('hello.html')

if __name__ == '__main__':
    socketio.run(app, debug=True)