from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "HEllo"


app.run(debug=True)
