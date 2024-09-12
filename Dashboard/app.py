from flask import Flask, request, redirect, session, render_template, jsonify
import requests
from flask import send_from_directory
from jinja2 import FileSystemLoader, ChoiceLoader

app = Flask(__name__)

app.secret_key = 'OMPzlveuVtk2k_xgkrv-OpbhkK2A0IRT'

DISCORD_CLIENT_ID = '1277964660339118111'
DISCORD_CLIENT_SECRET = "C:\Users\shake\Documents\GitHub\Mracci-Website\.env"
REDIRECT_URI = 'http://localhost:5000/callback'
DISCORD_API_URL = 'https://discord.com/api/v10'

linked_bots = {}

app.jinja_loader = ChoiceLoader([
    FileSystemLoader('Dashboard'),
    FileSystemLoader('Main Page')
])

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/login')
def login():
    return redirect(f'https://discord.com/oauth2/authorize?client_id={DISCORD_CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=code&scope=identify+guilds+bot')

@app.route('/callback')
def callback():
    code = request.args.get('code')
    if not code:
        return "Error: No code received", 400
    try:
        token = get_token(code)
        user_id = get_user_id(token)

        linked_bots[user_id] = True

        session['user_id'] = user_id
        session['access_token'] = token
        return redirect('/dashboard')
    except Exception as e:
        return f"Error retrieving token: {e}", 500

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session or not linked_bots.get(session['user_id'], False):
        return redirect('/')  

    return render_template('dashboard.html')  
@app.route('/check_connection')
def check_connection():
    user_id = session.get('user_id')
    if user_id and linked_bots.get(user_id, False):
        return jsonify({'connected': True})
    return jsonify({'connected': False})

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('access_token', None)
    return redirect('/')

def get_token(code):
    response = requests.post(f'{DISCORD_API_URL}/oauth2/token', data={
        'client_id': DISCORD_CLIENT_ID,
        'client_secret': DISCORD_CLIENT_SECRET,
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'scope': 'identify+guilds+bot'
    })

    if response.status_code != 200:
        error_info = response.json()
        raise ValueError(f"Failed to get token: {response.status_code} - {error_info.get('error_description', response.text)}")

    return response.json().get('access_token')

def get_user_id(token):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(f'{DISCORD_API_URL}/users/@me', headers=headers)
    if response.status_code != 200:
        raise ValueError(f"Failed to get user ID: {response.status_code} - {response.text}")
    return response.json().get('id')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
