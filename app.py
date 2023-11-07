from audioop import reverse
from pyradios import RadioBrowser
from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)
rb = RadioBrowser()

def radio_search(search):
    if search:
        radio = rb.search(name=search, name_exact = False)
        return radio
    else:
        return {} 
        
@app.route('/radio/<radioname>')
def show_user_profile(radioname):
    return jsonify(radio_search(radioname))
    
@app.route('/api',methods=['POST','GET'])
def get_radio_api():
    if request.method == "POST":
        data = json.loads(request.data)
        radio = radio_search(data['search'])
        return jsonify(radio)

@app.route('/', methods=['POST','GET'])

def home():
    radio_res = []
    if request.method == 'POST':
        search = request.form.get('search')
        if search:
            radio_res = radio_search(search)
            
    return render_template('index.html', res = radio_res)
@app.route('/2', methods=['POST','GET'])

def home2():
    radio_res = []
    if request.method == 'POST':
        search = request.form.get('search')
        if search:
            radio_res = radio_search(search)
            
    return render_template('index2.html', res = radio_res)
if __name__ == '__main__':
    app.run(debug=True)
