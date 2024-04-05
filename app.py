from flask import Flask, jsonify, request, send_file
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import io


app = Flask(__name__)
app.secret_key = "secret"
cred = credentials.Certificate("secret.json")
default_app = firebase_admin.initialize_app(cred, {'storageBucket': "doc-tracker-4791c.appspot.com"})
bucket = storage.bucket()

def test_storage():
    blob = bucket.blob('test.gif').download_as_string()
    return blob



@app.route('/', methods=['GET'])
def home():
    userAgent = request.headers['User-Agent']
    remoteAddr =  request.remote_addr
    print(f"{userAgent},  {remoteAddr}")
    blob = test_storage()
    return send_file(io.BytesIO(blob), mimetype='image/gif')




if __name__ == '__main__':
    app.debug=True
    app.run(host='127.0.0.1', port=5000)
