# app.py
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/page1')
def page1():
    return render_template('page1.html')

@socketio.on('audio_data')
def handle_audio(audio_data):
    # Broadcast the received audio data to all connected clients
    socketio.emit('audio_data', audio_data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
