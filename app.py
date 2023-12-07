# app.py
from flask import Flask, render_template, Response, request
from flask_socketio import SocketIO, emit
import base64

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/receiver')
def receiver():
    return render_template('receiver.html')

@socketio.on('audio_data')
def handle_audio(audio_data):
    emit('audio_data', audio_data, broadcast=True)

@app.route('/record_audio', methods=['POST'])
def record_audio():
    audio_data = request.data
    encoded_audio = base64.b64encode(audio_data).decode('utf-8')
    socketio.emit('audio_data', encoded_audio, broadcast=True)
    return "OK"

if __name__ == '__main__':
    socketio.run(app, debug=True)
