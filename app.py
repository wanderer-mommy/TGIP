from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello World!</h1><p>This is my first Python website.</p>"

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/about")
def about():
    return "<h2>About Me</h2><p>This site is built with Python.</p>"
