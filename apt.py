from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello_world():
    return "Hi! How are you?"

#debug = True : load automatically
if (__name__ == "__main__"):
    app.run(debug = True)