from flask import Flask, jsonify
import firebase_admin
from firebase_admin import credentials


app = Flask(__name__)
app.secret_key = "secret"
cred = credentials.Certificate("secret.json")
firebase_admin.initialize_app(cred)



@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Invalid password'}), 401




if __name__ == '__main__':
    app.debug=True
    default_app = firebase_admin.initialize_app()
    app.run(host='127.0.0.1', port=5000)
