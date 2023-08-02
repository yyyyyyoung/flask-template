from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def hello_world():
    return 'flask后端'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=False)
